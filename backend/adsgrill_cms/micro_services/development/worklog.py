from app.models import Users, Project, Sprint, Issue, LinkedIssue, WorkLog
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
import uuid
from datetime import timedelta, time,datetime
import re
from django.db.models import Sum
def convert_to_duration(duration_str):
    if 'h' not in duration_str:
        duration_str += ' 0h'
    if 'm' not in duration_str:
        duration_str += ' 0m'
    if 's' not in duration_str:
        duration_str += ' 0s'
    format = ["0h", "0m", "0s"]
    duration_str = duration_str.split(" ")
    match = 0
    for i in range(3):
        if format[i][-1] == duration_str[match][-1]:
            format[i] = duration_str[match]
            match += 1
    resultant_str = " ".join(format)
    regex = re.compile(r'(?:(?P<hours>\d+)h\s*)?(?:(?P<minutes>\d+)m\s*)?(?:(?P<seconds>\d+)s\s*)?$')
    match = regex.match(resultant_str)
    components = {key: int(value) if value else 0 for key, value in match.groupdict().items()}
    duration = timedelta(
        hours=components.get('hours', 0),
        minutes=components.get('minutes', 0),
        seconds=components.get('seconds', 0)
    )
    return duration
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
class WorklogView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            requestData = request.data
            if 'sprint_id' not in requestData or 'logged_time' not in requestData or 'issue_id' not in requestData:
                return JsonResponse({'message': 'Missing required fields'})
            sprint_instance = Sprint.objects.get(pk=requestData.get('sprint_id'))
            issue_instance = Issue.objects.get(pk=requestData.get('issue_id'))
            assignee_instance = request.user
            logged_time = requestData.get('logged_time')
            attachments = request.FILES.getlist('attachments', [])
            if issue_instance and issue_instance.assignee and issue_instance.assignee != assignee_instance:
                return JsonResponse({'message': 'Invalid User'})
            worklogs = WorkLog.objects.filter(issue=issue_instance).order_by('-created_at')
            if worklogs:
                saved_logged_time = worklogs.aggregate(Sum('logged_time'))['logged_time__sum']
            else:
                saved_logged_time = timedelta(0)
            checkDays = issue_instance.exp_duration - (saved_logged_time)
            if checkDays.days:
                upd_logged_time = convert_to_duration(logged_time)+convert_to_duration('16h 30m 0s')
            else:
                upd_logged_time = convert_to_duration(logged_time)
            remaining_time = issue_instance.exp_duration-(saved_logged_time+upd_logged_time)
            if remaining_time < timedelta(0):
                remaining_time = timedelta(0)
            with transaction.atomic():
                worklog_instance = WorkLog.objects.create(
                    sprint=sprint_instance,
                    issue=issue_instance,
                    author=assignee_instance,
                    logged_time=upd_logged_time,
                    description=requestData.get('description'),
                    remaining_time=remaining_time
                )
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'worklog', str(worklog_instance.pk))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    file_extension = attachment.name.split('.')[-1]
                    unique_id = str(uuid.uuid4().hex[:6])
                    unique_filename = f"{unique_id}_{worklog_instance.pk}.{file_extension}"
                    attachment_path = os.path.join(subdirectory, unique_filename)
                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)
                    attachment_file_names.append(attachment_path)
                worklog_instance.attachment = attachment_file_names
                worklog_instance.save()
        except Sprint.DoesNotExist:
            return JsonResponse({'message': "Requested Sprint not exist"})
        except Issue.DoesNotExist:
            return JsonResponse({'message': "Requested Issue not exist"})
        except Exception as e:
            transaction.set_rollback(True)
            return JsonResponse({'error': str(e)})
        return JsonResponse({'message': 'Worklog created successfully'},status=status.HTTP_200_OK)
    def get(self, request):
        try:
            issue_id = request.data.get('issue_id')
            issue_instance = Issue.objects.get(pk=issue_id)
            worklogs = WorkLog.objects.filter(issue=issue_instance).order_by('-created_at')
            if worklogs:
                saved_logged_time = worklogs.aggregate(Sum('logged_time'))['logged_time__sum']
                remaining_time = issue_instance.exp_duration - saved_logged_time
                if remaining_time < timedelta(0):
                    remaining_time = timedelta(0)
                data = [{
                    "author": worklog.author.name,
                    "sprint": worklog.sprint.pk,
                    "issue": worklog.issue.pk,
                    "description": worklog.description,
                    "logged_time": worklog.logged_time,
                    "status":worklog.issue.status,
                    "created_at": worklog.created_at,
                    "remaining_time":issue_instance.exp_duration-worklog.logged_time,
                    "attachments": worklog.attachment
                } for worklog in worklogs]
                data.append({'all_logged_time':saved_logged_time, 'final_remaining_time':remaining_time})
                response = JsonResponse({"Data": data}, status=status.HTTP_200_OK)
            else:
                response = JsonResponse({"message":"No worklogs found for this issue"}, status=status.HTTP_204_NO_CONTENT)
        except Issue.DoesNotExist:
            return JsonResponse({"message": "Issue instance not exists"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
    def put(self, request):
        try:
            requestData = request.data
            upd_worklog = WorkLog.objects.get(pk=requestData.get('id'))
            logged_time = requestData.get('logged_time')
            attachments = request.FILES.getlist('attachments', [])
            description = requestData.get('description') if requestData.get('description') else None
            if upd_worklog.created_at.date() != datetime.now().date():
                return JsonResponse({"message": "You can update worklog at the same day only"})
            issue_instance = upd_worklog.issue
            worklogs = WorkLog.objects.filter(issue=issue_instance).order_by('-created_at')
            if worklogs:
                saved_logged_time=worklogs.exclude(pk=upd_worklog.pk).aggregate(Sum('logged_time'))['logged_time__sum']
            else:
                saved_logged_time = timedelta(0)
            checkDays = issue_instance.exp_duration-saved_logged_time
            if checkDays.days:
                upd_logged_time = convert_to_duration(logged_time)+convert_to_duration('16h 30m 0s')
            else:
                upd_logged_time = convert_to_duration(logged_time)
            with transaction.atomic():
                upd_worklog.logged_time = upd_logged_time
                upd_worklog.description = description
                attachment_files_list = []
                if attachments:
                    for attachment in attachments:
                        subdirectory = os.path.join('media', 'uploads', 'Development', 'worklog', str(upd_worklog.pk))
                        if not os.path.exists(subdirectory):
                            os.makedirs(subdirectory)
                        file_extension = attachment.name.split('.')[-1]
                        unique_id = uuid.uuid4().hex[:6]
                        unique_filename = f"{unique_id}_{str(upd_worklog.pk)}.{file_extension}"
                        attachment_path = os.path.join(subdirectory, unique_filename)
                        with open(attachment_path, 'wb') as destination:
                            for chunk in attachment.chunks():
                                destination.write(chunk)
                        attachment_files_list.append(attachment_path)
                upd_worklog.attachment.extend(attachment_files_list)
                upd_worklog.save()
        except WorkLog.DoesNotExist:
            return JsonResponse({'message': "Requested worklog not exists"})
        except Sprint.DoesNotExist:
            return JsonResponse({'message':'Requested sprint not exists'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({"message": "Worklog updated successfully"})
    def delete(self, request):
        try:
            del_worklog = WorkLog.objects.get(pk=request.data.get('id'))
            file_paths = del_worklog.attachment
            if file_paths:
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        os.remove(file_path)
            directory = str(del_worklog.pk)
            directory_path = os.path.join("media\\uploads\\Development\\worklog\\", directory)
            if os.path.exists(directory_path):
                os.rmdir(directory_path)
            del_worklog.delete()
        except WorkLog.DoesNotExist:
            return JsonResponse({'message': "Requested worklog not exists"})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({"message": "Worklog deleted successfully"})