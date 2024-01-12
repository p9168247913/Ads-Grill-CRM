from app.models import Project, Users, Client, Sprint
from rest_framework.views import APIView
from django.utils import timezone
import os
from rest_framework import status
from django.http import JsonResponse
import json
from django.db import transaction
from django.db.utils import IntegrityError
from django.db.models import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage
from braces.views import CsrfExemptMixin
from io import BytesIO
import zipfile
from django.http import HttpResponse

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class ProjectView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]
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
            progress = requestData.get('progress')
            team_members = requestData.get('team_members')
            host_address = requestData.get('host_address')
            tech_stacks = requestData.get('tech_stacks')

            if Project.objects.filter(name=name).exists():
                    return JsonResponse({'message':'Project with this name already exists'})
            
            with transaction.atomic():
                team_lead_instance = Users.objects.get(pk=team_lead_id) if team_lead_id else None
                client_instance = Client.objects.get(pk=client_id)
                reporter_instance=Users.objects.get(pk=reporter_id)
                    
                project_instance = Project.objects.create(
                    reporter=reporter_instance,
                    team_lead=team_lead_instance,
                    client=client_instance,
                    name=name,
                    key=key,
                    type=type,
                    status=pro_status,
                    progress=progress,
                    team_members=team_members,
                    host_address=host_address,
                    tech_stacks=tech_stacks,
                )
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'projects', str(project_instance.name))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
                    unique_filename = f"{timestamp}_{attachment.name}"
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
            import traceback
            traceback.print_exc()
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Created Successfully'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            all_projects = Project.objects.all().order_by('-created_at')
            res_data = [{
                "id": project.pk,
                "reporter": project.reporter.name if project.reporter else None,
                "team_lead": project.team_lead.name if project.team_lead else None,
                "client": project.client.name if project.client else None,
                "name": project.name,
                "key": project.key,
                "type": project.type,
                "status": project.status,
                "attachments": project.attachments,
                "progress": project.progress,
                "team_members": project.team_members,
                "host_address": project.host_address,
                "tech_stacks": project.tech_stacks,
                "created_at": project.created_at,
            }for project in all_projects]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'projects':res_data}, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            req_data = request.data
            reporter_instance = Users.objects.get(pk=req_data.get('reporter_id'))
            team_lead_instance = Users.objects.get(pk=req_data.get('team_lead_id')) if req_data.get('team_lead_id') else None
            client_instance = Client.objects.get(pk=req_data.get('client_id'))
            upd_project = Project.objects.get(pk=req_data.get('id'))
            upd_project.reporter = reporter_instance
            upd_project.team_lead = team_lead_instance
            upd_project.client = client_instance
            upd_project.name = req_data.get('name')
            upd_project.key = req_data.get('key')
            upd_project.type = req_data.get('type')
            upd_project.status = req_data.get('status', 'to_do')  
            upd_project.attachments = req_data.get('attachments', []) 
            upd_project.progress = req_data.get('progress')
            upd_project.team_members = req_data.get('team_members')
            upd_project.host_address = req_data.get('host_address')
            upd_project.tech_stacks = req_data.get('tech_stacks')
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
                del_project.delete()

        except ObjectDoesNotExist:
            return JsonResponse({'message':'Requested Project Does Not Exists'}, status=status.HTTP_204_NO_CONTENT)        
        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Deleted Successfully'}, status=status.HTTP_404_NOT_FOUND)
    
class DownloadProjectAttchments(APIView):
    def get(self,request):
        try:
            id=request.GET.get("id")
            project_instance=Project.objects.get(pk=id)
            files=project_instance.attachments
            
            zip_buffer=BytesIO()
            with zipfile.ZipFile(zip_buffer,'w') as pro_zip:
                for file in files:
                    file_name = file.split("\\")[-1]
                    pro_zip.write(file, file_name)
            response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename={project_instance.name}_attachments.zip'
            
            return response
            
        except Exception as e:
            return JsonResponse({"message":str(e)})
    

class GetLeadManagers(APIView):
    def get(self, request):
        try:
            all_lead_man = Users.objects.filter(role__name='Development', designation='Product Manager', is_deleted=False).order_by("-created_at")
            res_data = [{
                "id":lead_man.pk,
                "name":lead_man.name
            }for lead_man in all_lead_man]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'lead_man':res_data}, status=status.HTTP_200_OK)



