from app.models import Project, Users, Client
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
import json
from django.db import transaction
from django.db.utils import IntegrityError
from django.db.models import ObjectDoesNotExist

class ProjectView(APIView):
    def post(self, request):
        try:
            requestData = json.loads(request.body)
            client_id = requestData.get('client_id')
            name = requestData.get('name')
            key = requestData.get('key')
            type = requestData.get('type')
            pr_status = requestData.get('status')
            lead_man_id = requestData.get('lead_man_id')

            if Project.objects.filter(name=name, is_deleted=False).exists():
                    return JsonResponse({'message':'Project with this name already exists'})
            
            with transaction.atomic():
                lead_instance = Users.objects.get(pk=lead_man_id)
                client_instance = Client.objects.get(pk=client_id)

                project_instance = Project.objects.create(
                     client = client_instance,
                     name = name,
                     key = key,
                     type = type,
                     status = pr_status,
                     lead = lead_instance
                )

                project_instance.save()

        except IntegrityError as i:
            return JsonResponse({'messge':str(i)})
        
        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Created Successfully'}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            all_projects = Project.objects.filter(is_deleted=False).order_by('-created_at')
            res_data = [{
                "id":project.pk,
                "client": project.client.name,
                "name":project.name,
                "key":project.key,
                "type":project.type,
                "status":project.status,
                "lead_man": project.lead.name,
                "start_date":project.created_at
            }for project in all_projects]
        except Exception as e:
            return JsonResponse({'message':str(e)})
        return JsonResponse({'projects':res_data}, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            req_data = json.loads(request.body)
            lead_man_instance = Users.objects.get(pk=req_data.get('lead_man_id'))
            upd_project = Project.objects.get(pk=req_data.get('id'))
            upd_project.name = req_data.get('name')
            upd_project.key = req_data.get('key')
            upd_project.type = req_data.get('type')
            upd_project.status = req_data.get('status')
            upd_project.lead = lead_man_instance
            upd_project.save()

        except Users.DoesNotExist:
            return JsonResponse({'message':'Requested lead Manager does not exists'}, status=status.HTTP_404_NOT_FOUND)
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
                del_project.is_deleted = True
                del_project.save()

        except ObjectDoesNotExist:
            return JsonResponse({'message':'Requested Project Does Not Exists'}, status=status.HTTP_204_NO_CONTENT)        
        except Exception as e:
            return JsonResponse({'message':str(e)})
        
        return JsonResponse({'message':'Project Deleted Successfully'}, status=status.HTTP_404_NOT_FOUND)
    

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



