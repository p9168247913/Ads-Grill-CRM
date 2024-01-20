from app.models import Users,Project,Sprint,Issue,LinkedIssue
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from django.db import transaction
import os
from django.utils import timezone
from rest_framework import status
import zipfile
from django.http import HttpResponse
from io import BytesIO
import uuid
from django.db.models import Sum
from datetime import timedelta
import re


def convert_to_duration(duration_str):
    if 'd' not in duration_str:
        duration_str+=' 0d'
    if 'h' not in duration_str:
        duration_str+=' 0h'
    if 'm' not in duration_str:
        duration_str+=' 0m'
    regex = re.compile(r'(?:(?P<weeks>\d+)w )?(?:(?P<days>\d+)d )?(?:(?P<hours>\d+)h )?(?:(?P<minutes>\d+)m)?')

    match = regex.match(duration_str)
    components = {key: int(value) if value else 0 for key, value in match.groupdict().items()}

    duration = timedelta(
        weeks=components.get('weeks', 0),
        days=components.get('days', 0),
        hours=components.get('hours', 0),
        minutes=components.get('minutes', 0)
    )
    return duration

class IssueView(APIView):
    def post(self, request):
        try:
            requestData = request.data 
            project_id = requestData.get('project_id')
            sprint_id = requestData.get('sprint_id')
            reporter_id = requestData.get('reporter_id')
            team_lead_id = requestData.get('team_lead_id')
            title = requestData.get('title')
            description = requestData.get('description')
            type = requestData.get('type')
            priority = requestData.get('priority')
            status = requestData.get('status')
            attachments = request.FILES.getlist('attachments', [])
            assignee_ids=requestData.get('assignee_ids',[])
            parent_issue_ids=requestData.get('parent_issue_ids',[])
            exp_duration = requestData.get('exp_duration')
            linked_issues=requestData.get('linked_issues',[])
            linked_issue_type=requestData.get('linked_issue_type')
            
            sprint_instance = Sprint.objects.get(pk=sprint_id)
            sprint_exp_duration=sprint_instance.exp_duration
                
            issue_exp_duration = convert_to_duration(exp_duration)
            existing_issue_duration=Issue.objects.filter(sprint=sprint_instance).aggregate(Sum('exp_duration'))['exp_duration__sum']
            
            total_duration = issue_exp_duration + existing_issue_duration

            if total_duration > sprint_exp_duration:
                return JsonResponse({"message": "Related issues durations for this sprint exceeds the sprint duration length ,please update sprint duration"})

            if Issue.objects.filter(title=title, project=project_id).exists():
                return JsonResponse({"message": "Issue with this title already exists"})

            
            with transaction.atomic():
                project_instance = Project.objects.get(pk=project_id)
                reporter_instance = Users.objects.get(pk=reporter_id)
                team_lead_instance = Users.objects.get(pk=team_lead_id) if team_lead_id else None
                
                issue_instance = Issue.objects.create(
                    project=project_instance,
                    sprint=sprint_instance,
                    reporter=reporter_instance,
                    team_lead=team_lead_instance,
                    title=title,
                    description=description,
                    type=type,
                    priority=priority,
                    status=status,
                    exp_duration=exp_duration
                )
                if assignee_ids:
                    assignee_ids=assignee_ids.split(',')
                    assignees = Users.objects.filter(pk__in=assignee_ids)
                    issue_instance.assignee.add(*assignees)
                    
                    
                
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'issues', str(f"{project_instance.key}_{sprint_instance.key}_{issue_instance.title}"))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                        
                    file_extension = attachment.name.split('.')[-1]
                    unique_id = str(uuid.uuid4().hex[:6])
                    unique_filename = f"{unique_id}_{issue_instance.key}.{file_extension}"
                    attachment_path = os.path.join(subdirectory, unique_filename)
                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                    attachment_file_names.append(attachment_path)

                issue_instance.attachments = attachment_file_names
                issue_instance.save()
                
                 
                if parent_issue_ids:
                    parent_issue_ids=parent_issue_ids.split(',')    
                    parent_issues = Issue.objects.filter(pk__in=parent_issue_ids)
                    issue_instance.parent_issue.add(*parent_issues)
                    
                    issue_instance.save()

                
                
                if linked_issues:
                    linked_issue_instances = LinkedIssue.objects.create(
                        project=project_instance,
                        sprint=sprint_instance,
                        destination=issue_instance,
                        type=linked_issue_type
                    )
                    
                    linked_issues = linked_issues.split(',')
                    try:
                        for linked_issue_id in linked_issues:
                            linked_issue_instance = Issue.objects.get(pk=linked_issue_id)
                            linked_issue_instances.source.add(linked_issue_instance)
                    except ObjectDoesNotExist:
                        return JsonResponse({"message":"Requested Issue do not exists"})

                    linked_issue_instances.save()
                   
        except Project.DoesNotExist:
            return JsonResponse({"message": "Requested Project not exists"})

        except Sprint.DoesNotExist:
            return JsonResponse({"message": "Requested Sprint not exists"})

        except Users.DoesNotExist:
            return JsonResponse({"message": "Requested User not exists"})

        return JsonResponse({"message": "Issue created successfully"})
    
    def get(self,request):
        try:
            project_instance=Project.objects.get(pk=request.data.get('id'))
            all_issues=Issue.objects.filter(project=project_instance).order_by('-created_at')
            if not all_issues.exists():
                return JsonResponse({"message":"No issues on this project"})
            data = []
            for issue in all_issues:
                assignees_data = [{
                    "id": assignee.id,
                    "name": assignee.name
                } for assignee in issue.assignee.all()]

                issue_data = {
                    "project": issue.project.name,
                    "sprint": issue.sprint.name,
                    "reporter": issue.reporter.name,
                    "team_lead": issue.team_lead.name if issue.team_lead else None,
                    "title": issue.title,
                    "key": issue.key,
                    "description": issue.description,
                    "type": issue.type,
                    "priority": issue.priority,
                    "status": issue.status,
                    "attachments": issue.attachments,
                    "exp_duration": issue.exp_duration,
                    "org_duration": issue.org_duration,
                    "created_at": issue.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "assignees": assignees_data
                }
                
                data.append(issue_data)
            
        except Exception as e:
            return JsonResponse({str(e)})    
        
        return JsonResponse({"issues":data},status=status.HTTP_200_OK)
    
    def put(self,request):
        try:
            requestData=request.data
            upd_issue=Issue.objects.get(pk=requestData.get('id'))
            project_instance=Project.objects.get(pk=requestData.get('project_id'))
            sprint_instance=Sprint.objects.get(pk=requestData.get('sprint_id'))
            reporter_instance=Users.objects.get(pk=requestData.get('reporter_id'))
            team_lead_instance=Users.objects.get(pk=requestData.get("team_lead_id")) if requestData.get('team_lead_id') else None
            parent_issue_ids=requestData.get('parent_issue_ids',[])
            attachments = request.FILES.getlist('attachments', [])
            assignee_ids=requestData.get('assignee_ids',[]) if requestData.get('assignee_ids') else None
            
            sprint_exp_duration=sprint_instance.exp_duration
            issue_exp_duration = convert_to_duration(request.data.get('exp_duration'))
            existing_issue_duration=Issue.objects.filter(sprint=sprint_instance).aggregate(Sum('exp_duration'))['exp_duration__sum']
            
            total_duration = issue_exp_duration + existing_issue_duration

            if total_duration > sprint_exp_duration:
                return JsonResponse({"message": "Related issues durations for this sprint exceeds the sprint duration length ,please update sprint duration"})

            
            with transaction.atomic():
                upd_issue.sprint=sprint_instance
                upd_issue.project=project_instance
                upd_issue.reporter=reporter_instance
                upd_issue.team_lead=team_lead_instance
                upd_issue.title=requestData.get('title')
                upd_issue.key=requestData.get('key')
                upd_issue.description=requestData.get('description')
                upd_issue.type=requestData.get('type')
                upd_issue.priority=requestData.get('priority')
                upd_issue.exp_duration=requestData.get('exp_duration')
                upd_issue.org_duration=requestData.get('org_duration')

                
                upd_issue.assignee.clear()
                upd_issue.parent_issue.clear()
                if assignee_ids or parent_issue_ids:
                    assignee_ids=assignee_ids.split(',')
                    assignees = Users.objects.filter(pk__in=assignee_ids)
                    upd_issue.assignee.add(*assignees)
                    
                    parent_issue_ids=parent_issue_ids.split(',')    
                    parent_issues = Issue.objects.filter(pk__in=parent_issue_ids)
                    upd_issue.parent_issue.add(*parent_issues)


                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'issues', str(f"{project_instance.key}_{sprint_instance.key}_{upd_issue.title}"))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    file_extension = attachment.name.split('.')[-1]
                    unique_id = str(uuid.uuid4().hex[:6])
                    unique_filename = f"{unique_id}_{upd_issue.key}.{file_extension}"
                    attachment_path = os.path.join(subdirectory, unique_filename)
                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                    attachment_file_names.append(attachment_path)
                upd_issue.attachments.extend(attachment_file_names)
                
                upd_issue.save()
                
        except Project.DoesNotExist:
            return JsonResponse({"message":"Requested Project not exists"})
        except Sprint.DoesNotExist:
            return JsonResponse({"message":"Requested Sprint not exists"})
        except Users.DoesNotExist:
            return JsonResponse({"message":"Requested User not exists"})
        except Exception as e:
            return JsonResponse({"message":str(e)})
        return JsonResponse({"message":"issue Updated successfully"})
    
    def delete(self,request):
        try:
            issue_instance=Issue.objects.get(pk=request.GET.get('id'))
            issue_instance.delete()
        except Issue.DoesNotExist:
            return JsonResponse({"message":"Request Issue not exists"})
        return JsonResponse({"message":"issue deleted successfully"})
    
class LinkedIssueView(APIView):
    def post(self,request):
        try:
            requestData=request.data
            project_id=requestData.get("project_id")
            sprint_id=requestData.get("sprint_id")
            source_ids=requestData.get("source_ids",[])
            destination_id=requestData.get("destination_id")
            type=requestData.get("type") if requestData.get("type") else None
            
            project_instance=Project.objects.get(pk=project_id)
            sprint_instance=Sprint.objects.get(pk=sprint_id)
            destination_instance=Issue.objects.get(pk=destination_id)
            
            if source_ids:
                check_source_ids=source_ids.split(',')
                for source_id in check_source_ids:
                    check_exists=LinkedIssue.objects.filter(
                        source=source_id,
                        destination=destination_instance
                    ).exists()

                    if check_exists:
                        return JsonResponse({"message":"issue already mapped"})
            
            linked_issue_instance=LinkedIssue.objects.create(
                project=project_instance,
                sprint=sprint_instance,
                destination=destination_instance,
                type=type
            )
            
            if source_ids:
                source_ids=source_ids.split(',')
                for source_id in source_ids:
                    issue_instance=Issue.objects.get(pk=source_id)
                    linked_issue_instance.source.add(issue_instance)
                    
            linked_issue_instance.save()

            
        except Project.DoesNotExist:
            return JsonResponse({"message":"Requested Project not exists"})
        
        except Sprint.DoesNotExist:
            return JsonResponse({"message":"Requested Sprint not exists"})
        
        except Issue.DoesNotExist:
            return JsonResponse({"message":"Requested Issue not exists"})
        
        except Exception as e:
            return JsonResponse({"errror":str(e)})
        
        return JsonResponse({"message":"Linked_issue Created successfully "})
    
class DownloadIssuesAttchments(APIView):
    def get(self,request):
        try:
            id=request.GET.get("id")
            issue_instance=Issue.objects.get(pk=id)
            files=issue_instance.attachments
            
            zip_buffer=BytesIO()
            with zipfile.ZipFile(zip_buffer,'w') as pro_zip:
                for file in files:
                    file_name = file.split("\\")[-1]
                    pro_zip.write(file, file_name)
            response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={issue_instance.title}_attachments.zip'
            
            return response
            
        except Exception as e:
            return JsonResponse({"message":str(e)})
    