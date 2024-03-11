from app.models import Project, Users, Client, Sprint, Issue
from rest_framework.views import APIView
from django.utils import timezone
import os
from rest_framework import status
from django.http import JsonResponse
import json
from django.db import transaction
from django.db.utils import IntegrityError
from django.db.models import ObjectDoesNotExist, Count, Sum, Case, When, F, Value, IntegerField
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.core.files.storage import default_storage
from braces.views import CsrfExemptMixin
from io import BytesIO
import zipfile
from django.http import HttpResponse
from django.db.models import Q
import uuid

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class CustomSessionAuthentication(SessionAuthentication):
    def authenticate(self, request):
        user_auth_tuple = super().authenticate(request)
        if user_auth_tuple is None:
            raise AuthenticationFailed('Your session has expired. Please log in again.')
        return user_auth_tuple

class ProjectView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            requestData = request.data
            reporter_id = requestData.get('reporter_id')
            team_lead_id = requestData.get('team_lead_id')
            client_id = requestData.get('client_id')
            name = requestData.get('name')
            key = requestData.get('key')
            type = requestData.get('type')
            pro_status = requestData.get('status', 'to_do') 
            attachments = request.FILES.getlist('attachments', [])
            # team_members = requestData.get('team_members')
            host_address = requestData.get('host_address')
            tech_stacks = requestData.get('tech_stacks')

            if Project.objects.filter(name=name).exists():
                    return JsonResponse({'message':'Project with this name already exists'})
            
            with transaction.atomic():
                team_lead_instance = Users.objects.get(pk=team_lead_id) if team_lead_id else None
                client_instance = Users.objects.get(pk=client_id)
                reporter_instance=Users.objects.get(pk=reporter_id)
                    
                project_instance = Project.objects.create(
                    reporter=reporter_instance,
                    team_lead=team_lead_instance,
                    client=client_instance,
                    name=name,
                    key=key,
                    type=type,
                    status=pro_status,
                    # team_members=team_members,
                    host_address=host_address,
                    tech_stacks=tech_stacks,
                )
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'projects', str(project_instance.name))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    file_extension = attachment.name.split('.')[-1]
                    unique_id = str(uuid.uuid4().hex[:6])
                    unique_filename = f"{unique_id}_{project_instance.key}.{file_extension}"
                    attachment_path = os.path.join(subdirectory, unique_filename)

                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                    attachment_file_names.append(attachment_path)

                project_instance.attachments = attachment_file_names
                project_instance.save()

        except Client.DoesNotExist:
            return JsonResponse({"message":"Requested client does not exist"})
        
        except Users.DoesNotExist:
            return JsonResponse({"message":"Requested reporter does not exist"})
        
        except IntegrityError as i:
            return JsonResponse({'messge':str(i)})
        
        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Created Successfully'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            val = request.GET.get('key')
            res_data = []
            if val == 'development':
                all_projects = Project.objects.annotate(total_issues=Count('issue'), done_issues = Sum(Case(When(issue__status='done', then=1), default=Value(0), output_field=IntegerField()))).order_by('-created_at')
                for project in all_projects:
                    project_data = {
                        "id": project.pk,
                        "reporter": {
                            'id': project.reporter.pk if project.reporter else None,
                            'name': project.reporter.name if project.reporter else None
                        },
                        "team_lead": {
                            'id': project.team_lead.pk if project.team_lead else None,
                            'name': project.team_lead.name if project.team_lead else None
                        },
                        "client": {
                            'id': project.client.pk if project.client else None,
                            'name': project.client.name if project.client else None
                        },
                        "name": project.name,
                        "key": project.key,
                        "type": project.type,
                        "status": project.status,
                        "attachments": project.attachments,
                        "progress": int((project.done_issues*100) / project.total_issues) if project.total_issues > 0 else int(0),
                        "team_members": ", ".join(project.issue_set.values_list('assignee__name', flat=True).distinct()),
                        "host_address": project.host_address,
                        "tech_stacks": project.tech_stacks,
                        "created_at": project.created_at,
                    }
                    res_data.append(project_data)
            if val == 'client':
                clientID = request.GET.get('clientID')
                if not clientID:
                    return JsonResponse({'messgae':'Request parameter missing(clientID)'}, status=status.HTTP_400_BAD_REQUEST)
                client_all_projects = Project.objects.annotate(total_sprints=Count('sprint'), done_sprints=Sum(Case(When(sprint__status='done', then=1),default=Value(0), output_field=IntegerField()))).filter(client_id=clientID).order_by('-created_at')
                for project in client_all_projects:
                    sprints = Sprint.objects.filter(project_id = project.pk).order_by('-created_at')
                    project_data = {
                        "id": project.pk,
                        "reporter": {
                            'id': project.reporter.pk if project.reporter else None,
                            'name': project.reporter.name if project.reporter else None
                        },
                        "name": project.name,
                        "type": project.type,
                        "status": project.status,
                        "attachments": project.attachments,
                        "progress":int((project.done_sprints*100) / project.total_sprints) if project.total_sprints > 0 else int(0),
                        "host_address": project.host_address,
                        "tech_stacks": project.tech_stacks,
                        "created_at": project.created_at,
                        "sprints":[{
                            'id':sprint.pk,
                            'name':sprint.name,
                            'key':sprint.key,
                            'status':sprint.status,
                            'is_started':sprint.is_started,
                            'start_date':sprint.start_date
                            }for sprint in sprints]
                    }
                    res_data.append(project_data)

        except Project.DoesNotExist:
            return JsonResponse({'message':"No projects found"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'projects':res_data}, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            req_data = request.data
            attachments = request.FILES.getlist('attachments', [])
            reporter_instance = Users.objects.get(pk=req_data.get('reporter_id'))
            team_lead_instance = Users.objects.get(pk=req_data.get('team_lead_id')) if req_data.get('team_lead_id') else None
            client_instance = Users.objects.get(pk=req_data.get('client_id'))
            upd_project = Project.objects.get(pk=req_data.get('id'))
            with transaction.atomic():
                upd_project.reporter = reporter_instance
                upd_project.team_lead = team_lead_instance
                upd_project.client = client_instance
                upd_project.name = req_data.get('name')
                upd_project.key = req_data.get('key')
                upd_project.type = req_data.get('type')
                upd_project.status = req_data.get('status', 'to_do')  
                upd_project.host_address = req_data.get('host_address')
                upd_project.tech_stacks = req_data.get('tech_stacks')
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'projects', str(upd_project.name))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    file_extension = attachment.name.split('.')[-1]
                    unique_id = str(uuid.uuid4().hex[:6])
                    unique_filename = f"{unique_id}_{upd_project.key}.{file_extension}"
                    attachment_path = os.path.join(subdirectory, unique_filename)

                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                    attachment_file_names.append(attachment_path)

                upd_project.attachments.extend(attachment_file_names)
                upd_project.save()
            
        except Client.DoesNotExist as e:
            return JsonResponse({'message':"Client field is required"}, status=status.HTTP_404_NOT_FOUND)
        
        except Users.DoesNotExist as e:
            return JsonResponse({'message':"Reporter field is required"}, status=status.HTTP_404_NOT_FOUND)
            
        except Project.DoesNotExist:
            return JsonResponse({'message':'Requested project does not exists'}, status=status.HTTP_404_NOT_FOUND)
        except IntegrityError as i:
            return JsonResponse({'message':str(i)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message':str(e)}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message':'Project Updated Successfully'}, status=status.HTTP_200_OK)
    
    def delete(self, request):
        try:
            with transaction.atomic():
                id = request.GET.get('id')
                del_project = Project.objects.get(pk=id)

                file_paths = del_project.attachments
                if file_paths:
                    for file_path in file_paths:
                        if os.path.exists(file_path):
                            os.remove(file_path)
                directory = del_project.name
                directory_path = os.path.join("media\\uploads\\Development\\projects\\", directory)
                if os.path.exists(directory_path):
                    os.rmdir(directory_path)
                del_project.delete()

        except ObjectDoesNotExist:
            return JsonResponse({'message':'Requested Project Does Not Exists'}, status=status.HTTP_204_NO_CONTENT)        
        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Deleted Successfully'}, status=status.HTTP_404_NOT_FOUND)
    
class DownloadProjectAttchments(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            id=request.GET.get("id")
            project_instance=Project.objects.get(pk=id)
            files=project_instance.attachments
            if files:
                zip_buffer=BytesIO()
                with zipfile.ZipFile(zip_buffer,'w') as pro_zip:
                    for file in files:
                        file_name = file.split("\\")[-1]
                        pro_zip.write(file, file_name)
                response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename={project_instance.name}_attachments.zip'
            else:
                response = JsonResponse({"message":"No files found for the specified criteria."}, status=status.HTTP_204_NO_CONTENT)
           
        except IntegrityError as i:
            response =  JsonResponse({"message":str(i)})

        except Exception as e:
            response =  JsonResponse({"message":str(e)})
        return response
    

class GetProjectManagers(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            all_lead_man = Users.objects.filter(role__name='development', designation='project_manager', is_deleted=False).order_by("-created_at")
            res_data = [{
                "id":lead_man.pk,
                "name":lead_man.name
            }for lead_man in all_lead_man]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'project_managers':res_data}, status=status.HTTP_200_OK)
    
class GetAllAssignees(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            all_assignees = Users.objects.filter(Q(designation__icontains='developer'), role__name='development')
            res_data = [{
                'id':assignee.pk,
                'name': assignee.name
            } for assignee in all_assignees]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'assignees':res_data}, status=status.HTTP_200_OK)
    
class GetAllTeamLeaders(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            all_team_leaders = Users.objects.filter(Q(designation__icontains='team_lead'), role__name='development')
            res_data = [{
                'id':team_leader.pk,
                'name': team_leader.name
            } for team_leader in all_team_leaders]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'team_leaders':res_data}, status=status.HTTP_200_OK)

class GetAllClients(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            all_clients = Users.objects.filter(role__name='client',is_deleted=False).order_by("-created_at")
            res_data = [{
                "id":client.pk,
                "name":client.name
            }for client in all_clients]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'clients':res_data}, status=status.HTTP_200_OK)
        




