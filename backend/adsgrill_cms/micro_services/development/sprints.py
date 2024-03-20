from app.models import Users, Project, Sprint, Issue
from braces.views import CsrfExemptMixin
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from django.db.models import ObjectDoesNotExist
from django.db import transaction
import pandas as pd
import json
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.db.utils import IntegrityError
from os.path import basename
import os
import openpyxl
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, time
from django.db.models import Sum


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class SprintView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            requestData = request.data
            exp_duration = request.data.get('exp_duration')
            start_date_str = request.data.get('start_date')
            end_date_str = request.data.get('end_date')

            if Sprint.objects.filter(project__pk=requestData.get('project_id'), name=request.data.get('name')).exists():
                    return JsonResponse({'message':'Sprint with this name already exists'})
                
            if start_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M')
            else:
                start_date = None
            
            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M')
            else:
                end_date = None
            project_instance = Project.objects.get(pk=requestData.get('project_id'))
            reporter_instance = Users.objects.get(pk=requestData.get('reporter_id'))

            with transaction.atomic():
                sprint_instance = Sprint.objects.create(
                    project = project_instance,
                    reporter = reporter_instance,
                    name = requestData.get('name'),
                    key = requestData.get('key'),
                    description = requestData.get('description') if requestData.get('description') else None,
                    status = requestData.get('status') if requestData.get('status') else 'to_do',
                    exp_duration = exp_duration,
                    start_date = start_date,
                    end_date = end_date,
                    goal = requestData.get('goal') if requestData.get('end_date') else None,
                )
                sprint_instance.save()

        except Project.DoesNotExist:
            return JsonResponse({"message":"Requested project not found"}, status=404, safe=False)
        
        except Users.DoesNotExist:
            return JsonResponse({"message":"Requested product manager not found"}, status=404, safe=False)
        
        except IntegrityError as i:
            return JsonResponse({"message":str(i)})

        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({"message":"Sprint Created Successfully"}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
            val = request.GET.get('key')
            project_id = request.GET.get('id')
            if not val or not project_id:
                return JsonResponse({"messgae":"Bad request, required parameters not received"}, status=status.HTTP_400_BAD_REQUEST)
            if val == 'active_sprint':
                try:
                    activeSprintAndIssues = {}
                    activeSprint = Sprint.objects.get(project=project_id, is_started=True)
                    to_do_issues = Issue.objects.filter(sprint = activeSprint.pk, status='to_do').order_by('-created_at')
                    in_progress_issues = Issue.objects.filter(sprint = activeSprint.pk, status='in_progress').order_by('-created_at')
                    done_issues = Issue.objects.filter(sprint = activeSprint.pk, status='done').order_by('-created_at')

                    activeSprintData = {
                        "id":activeSprint.pk,
                        "name":activeSprint.name,
                    }
                    
                    to_do = [{
                        "id":to_do_issue.pk,
                        "title":to_do_issue.title,
                        "reporter":to_do_issue.reporter.name,
                        "status":to_do_issue.status
                    }for to_do_issue in to_do_issues]

                    in_progress = [{
                        "id":in_progress_issue.pk,
                        "title":in_progress_issue.title,
                        "reporter":in_progress_issue.reporter.name,
                        "status":in_progress_issue.status
                    }for in_progress_issue in in_progress_issues]

                    done = [{
                        "id":done_issue.pk,
                        "title":done_issue.title,
                        "reporter":done_issue.reporter.name,
                        "status":done_issue.status
                    }for done_issue in done_issues]
                    
                    activeSprintAndIssues['activeSprint'] = activeSprintData
                    activeSprintAndIssues['issues'] = {"to_do":to_do, "in_progress":in_progress, "done":done}

                    if not len(activeSprintAndIssues):
                        return JsonResponse({"message":"No data found in this project", "activeSprintAndIssues":activeSprintAndIssues}, status=status.HTTP_204_NO_CONTENT)
                
                except Sprint.DoesNotExist:
                    return JsonResponse({"message": "No active sprint found for this project"}, status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                    return JsonResponse({"message":str(e)})
                
                return JsonResponse({"activeSprintAndIssues":activeSprintAndIssues}, safe=False)
    
            if val == 'backlog':
                try:
                    sprintsAndIssues = []
                    sprints = Sprint.objects.filter(project=project_id).order_by('-created_at')
                    for sprint in sprints:
                        sprintData = {
                            "id": sprint.pk,
                            "name":sprint.name,
                            "is_started":sprint.is_started,
                            "exp_duration": sprint.exp_duration,
                            "project":{
                                "id":sprint.project.pk,
                                "name":sprint.project.name,
                                "key":sprint.project.key
                            },
                            "reporter":{
                                "id":sprint.reporter.pk,
                                "name":sprint.reporter.name
                            },
                            "key":sprint.key,
                            "description":sprint.description,
                            "status":sprint.status,
                            "start_date":sprint.start_date,
                            "end_date":sprint.end_date,
                            "goal":sprint.goal,
                            "issue_count": Issue.objects.filter(sprint=sprint.pk).count(),
                            "issues": None
                        }
                        issues = Issue.objects.filter(sprint=sprint.pk)
                        sprintData["issues"]= [{
                                "id":issue.pk,
                                "title": issue.title,
                                "status":issue.status,
                                "priority": issue.priority
                        }for issue in issues]
                        
                        sprintsAndIssues.append(sprintData)
                    
                    if not len(sprintsAndIssues):
                        return JsonResponse({"message":"No data found in this project", "sprintAndIssues":sprintsAndIssues}, status=status.HTTP_204_NO_CONTENT)
                    
                except Sprint.DoesNotExist:
                    return JsonResponse({"message": "No Sprint data found in this project"}, status=status.HTTP_204_NO_CONTENT)
                except Exception as e:
                    return JsonResponse({"message":str(e)})
                
                return JsonResponse({"sprintAndIssues":sprintsAndIssues}, safe=False)
            
    def put(self, request):
        try:
            requestData = request.data
            exp_duration = requestData.get('exp_duration')
            start_date_str = requestData.get('start_date')
            end_date_str = requestData.get('end_date')
            upd_sprint = Sprint.objects.get(pk=requestData.get('id'))
            is_started = requestData.get('is_started')
            if is_started == 'true':
                is_started = True
            if is_started == 'false':
                is_started = False

            if request.data.get('name') == upd_sprint.name:
                if Sprint.objects.filter(project__pk=requestData.get('project_id')).exists():
                    return JsonResponse({'message':'Sprint with this name already exists'})
            elif request.data.get('name') != upd_sprint.name:
                if Sprint.objects.filter(project__pk=requestData.get('project_id'), name=request.data.get('name')).exists():
                    return JsonResponse({'message':'Sprint with this name already exists'})
    
            if start_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M')
            else:
                start_date = None
    
            if end_date_str:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M')
            else:
                end_date = None
    
            reporter_instance = Users.objects.get(pk=requestData.get("reporter_id"))
            
            if(request.user.designation=="project_manager" and request.user.role.name=="development"):
                if requestData.get("status")=="done":
                   with transaction.atomic():
                        total_org_duration=Issue.objects.filter(sprint=upd_sprint).aggregate(Sum('org_duration'))['org_duration__sum']
                        upd_sprint.org_duration=total_org_duration
                        upd_sprint.is_started=False
                        upd_sprint.save()
    
            with transaction.atomic():
                upd_sprint.reporter = reporter_instance
                upd_sprint.key = requestData.get("key")
                upd_sprint.name = requestData.get("name")
                upd_sprint.description = requestData.get("description")
                upd_sprint.status = requestData.get("status")
                upd_sprint.exp_duration = exp_duration
                upd_sprint.start_date = start_date
                upd_sprint.end_date = end_date
                upd_sprint.goal = requestData.get('goal')
                upd_sprint.is_started = is_started
    
                upd_sprint.save()
    
        except Sprint.DoesNotExist:
            return JsonResponse({"message": "Requested Sprint not found"}, status=404)
    
        except Users.DoesNotExist:
            return JsonResponse({"message": "Requested User not found"}, status=404)
    
        except IntegrityError as i:
            return JsonResponse({"message": str(i)})
    
        except Exception as e:
            return JsonResponse({'message': str(e)})
    
        return JsonResponse({"message": "Sprint Updated Successfully"}, status=status.HTTP_200_OK)
    

    def delete(self,request):
        try:
            with transaction.atomic():
                id=request.GET.get('id')
                del_sprint=Sprint.objects.get(pk=id)
                del_sprint.delete()
            
        except ObjectDoesNotExist:
            return JsonResponse({'message':'Requested Sprint Does Not Exists'}, status=status.HTTP_204_NO_CONTENT)        
        except Exception as e:
            return JsonResponse({"message":str(e)})
        
        return JsonResponse({"message":"Sprint Deleted Successfuly"},status=status.HTTP_204_NO_CONTENT)