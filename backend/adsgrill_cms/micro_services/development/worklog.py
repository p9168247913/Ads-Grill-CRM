from app.models import Users,Project,Sprint,Issue,LinkedIssue,WorkLog
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from braces.views import CsrfExemptMixin
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


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
    
class WorklogView(CsrfExemptMixin,APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            requestData=request.data
            sprint_instance=Sprint.objects.get(pk=requestData.get('sprint_id'))
            issue_instance=Issue.objects.get(pk=requestData.get('issue_id')) if requestData.get('issue_id') else None
            author_instance=request.user
            logged_time=requestData.get('logged_time')
            attachments = request.FILES.getlist('attachments', [])
 
            if issue_instance.assignee != author_instance:
                return JsonResponse({'message':'invalid User'})
            
            
            remaining_time=issue_instance.exp_duration - convert_to_duration(logged_time)
            
            if remaining_time < convert_to_duration('0d 0h 0m'):
                return JsonResponse({'message':'time exceeds for this issue'})
        
            with transaction.atomic():
                worklog_instance=WorkLog.objects.create(
                    sprint=sprint_instance,
                    issue=issue_instance,
                    author=author_instance,
                    logged_time=logged_time,
                    description=requestData.get('description'),
                    remaining_time= logged_time
                )
                
                attachment_files_list=[]
                if attachments:
                    for attachment in attachments:
                        subdirectory = os.path.join('media', 'uploads', 'Development', 'worklog', f'worklog_{str(issue_instance.key)}')
                        if not os.path.exists(subdirectory):
                            os.makedirs(subdirectory)
                        file_extension = attachment.name.split('.')[-1]
                        unique_id = str(uuid.uuid4().hex[:6])
                        unique_filename = f"{unique_id}_{f'worklog_{str(issue_instance.key)}'}.{file_extension}"
                        attachment_path=os.path.join(subdirectory,unique_filename)
                        
                        with open (attachment_path,'wb') as destination:
                            for chunk in attachment.chunks():
                                destination.write(chunk)
                            
                        attachment_files_list.append(attachment_path)
                        
                worklog_instance.attachment=attachment_files_list
                worklog_instance.save()
            
        except Sprint.DoesNotExist:
            return JsonResponse({'message':"Requested Sprint not exist"})
        
        except Issue.DoesNotExist:
            return JsonResponse({'message':"Requested Issue not exist"})
        
        except Exception as e:
            return JsonResponse({'error':str(e)})
        
        return JsonResponse({'message':'worklog created successfully'})
    
    