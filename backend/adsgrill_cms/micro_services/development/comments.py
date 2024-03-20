from app.models import Project, Issue, Users, Sprint, Comment, LinkedIssue
from rest_framework.views import APIView
from rest_framework import status
import os
from django.http import JsonResponse, HttpResponse
from django.db.utils import IntegrityError
from django.db import transaction
from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from braces.views import CsrfExemptMixin
from io import BytesIO
import zipfile
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
    
class CommentsView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            currentUser = request.user
            requestData = request.data
            sprintID=None
            issueID=None
            value = requestData.get('key')
            if value == 'client':
                sprintID = requestData.get('sprintID')
                if not sprintID:
                    return JsonResponse({'message':'Invalid credentials(sprintID)'}, status=status.HTTP_400_BAD_REQUEST)
                sprintInstance = Sprint.objects.get(pk=sprintID)
                projectInstance = sprintInstance.project
            if value =='developers':
                issueID = requestData.get('issueID')
                if not issueID:
                    return JsonResponse({'message':'Invalid credentials(issueID)'}, status=status.HTTP_400_BAD_REQUEST)
                issueInstance = Issue.objects.get(pk=issueID)
                sprintInstance = issueInstance.sprint
                assignee = issueInstance.assignee
                projectInstance = issueInstance.project
            
            if currentUser.role.name == 'client' or currentUser.designation == 'project_manager' or assignee==currentUser:
                attachments = request.FILES.getlist('attachments', [])
                attachment_file_names = []
                if attachments:
                    if issueID:
                        subDirectory = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
                    if sprintID:
                         subDirectory = os.path.join('media', 'uploads', 'Development', 'client', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}"))
                    if not os.path.exists(subDirectory):
                        os.makedirs(subDirectory)
                    for attachment in attachments:
                        file_extension = attachment.name.split('.')[-1]
                        unique_id = str(uuid.uuid4().hex[:6])
                        if issueID:
                            unique_filename = f"{unique_id}_{issueInstance.key}.{file_extension}"
                        if sprintID:
                            unique_filename = f"{unique_id}_{sprintInstance.key}.{file_extension}"
                        attachment_path = os.path.join(subDirectory, unique_filename)

                        with open(attachment_path, 'wb') as destination:
                                for chunk in attachment.chunks():
                                    destination.write(chunk)

                        attachment_file_names.append(attachment_path)
                with transaction.atomic():
                    commentInstance = {
                            'author': currentUser,
                            'description': requestData.get('desc'),
                        }
                    if sprintID:
                        commentInstance['sprint'] = sprintInstance
                    if issueID:
                        commentInstance['issue'] = issueInstance
                    if attachment_file_names:
                        commentInstance['attachment'] = attachment_file_names
                    commentInstance = Comment.objects.create(**commentInstance)
            else:
                return JsonResponse({"message":"You dont have access to comment on other's issues"})
        except IndentationError as i:
            return JsonResponse({"error":str(i)})
        except Exception as e:
            return JsonResponse({"message":str(e)})

        return JsonResponse({"message":"Comment added succussfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        try:
            current_user_role = request.user.role.name
            current_user_designation = request.user.designation
            if not current_user_role:
                return JsonResponse({'message':"Anonymous user has no attribute role or unauthorized user"}, status=status.HTTP_401_UNAUTHORIZED)
            if not current_user_designation:
                return JsonResponse({'message':"Anonymous user has no attribute designation or unauthorized user"}, status=status.HTTP_401_UNAUTHORIZED)
            if current_user_role == 'client':
                sprintID = request.GET.get('sprintID')
                if not sprintID:
                    return JsonResponse({'message':'Invalid credentials(sprintID)'}, status=status.HTTP_400_BAD_REQUEST)
                sprintInstance = Sprint.objects.get(pk=sprintID)
                allComments = Comment.objects.filter(
                    Q(sprint=sprintInstance, author__role__name = 'client') |
                    Q(sprint=sprintInstance, author__role__name = 'development') &
                    Q(sprint=sprintInstance, author__designation = 'project_manager')
                    ).order_by('-created_at')

            if current_user_role == 'development':
                value = request.GET.get('key')
                if value == 'client':
                    sprintID = request.GET.get('sprintID')
                    if not sprintID:
                        return JsonResponse({'message':'Invalid credentials(sprintID)'}, status=status.HTTP_400_BAD_REQUEST)
                    sprintInstance = Sprint.objects.get(pk=sprintID)
                    allComments = Comment.objects.filter(
                        Q(sprint=sprintInstance, author__role__name='client') |
                        Q(sprint=sprintInstance, author__role__name='development') &
                        Q(sprint=sprintInstance, author__designation='project_manager')
                        ).order_by('-created_at')

                if value == 'developers':
                    issueID = request.GET.get('issueID')
                    if not issueID:
                        return JsonResponse({'message':'Invalid credentials(issueID)'}, status=status.HTTP_400_BAD_REQUEST)
                    issueInstance = Issue.objects.get(pk=issueID)
                    allComments = Comment.objects.filter(issue=issueInstance, author__role__name='development').order_by('-created_at')

            responseData = [{
                "commentID": comment.pk,
                "sprintID":comment.sprint.pk if comment.sprint else None,
                "IssueID":comment.issue.pk if comment.issue else None,
                "author":{
                    "id":comment.author.pk,
                    "name":comment.author.name,
                },
                "description":comment.description,
                "attachments":comment.attachment,
                "created_at":comment.created_at
            }for comment in allComments]

        except Exception as e:
            return JsonResponse({"message":str(e)})
        return JsonResponse({"comments":responseData}, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            requestData = request.data
            currentUser = request.user
            commentInstance = Comment.objects.get(pk=requestData.get('commentID'))
            desc = requestData.get('desc')
            issueInstance = commentInstance.issue
            sprintInstance = commentInstance.sprint
            if issueInstance:
                projectInstance = issueInstance.project
            if sprintInstance:
                projectInstance = sprintInstance.project

            if currentUser.role.name == 'client' or (currentUser.role.name == 'development' and currentUser.designation == 'project_manager') or commentInstance.issue.assignee == currentUser:
                attachments = request.FILES.getlist('attachments')
                attachment_file_names = []
                if attachments:
                    if issueInstance:
                        subDirectory = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
                    if sprintInstance:
                       subDirectory = os.path.join('media', 'uploads', 'Development', 'client', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}")) 
                    if not os.path.exists(subDirectory):
                        os.makedirs(subDirectory)
                    for attachment in attachments:
                        file_extension = attachment.name.split('.')[-1]
                        unique_id = str(uuid.uuid4().hex[:6])
                        if issueInstance:
                            unique_filename = f"{unique_id}_{issueInstance.key}.{file_extension}"
                        if sprintInstance:
                            unique_filename = f"{unique_id}_{sprintInstance.key}.{file_extension}"
                        attachment_path = os.path.join(subDirectory, unique_filename)

                        with open(attachment_path, 'wb') as destination:
                                for chunk in attachment.chunks():
                                    destination.write(chunk)

                        attachment_file_names.append(attachment_path)
                with transaction.atomic():
                    commentInstance.description = desc
                    if attachment_file_names:
                        commentInstance.attachment.extend(attachment_file_names)
                    commentInstance.save()
            else:
                return JsonResponse({'message':"You dont have access to make changes in comment on other's issues"})
        except IntegrityError as i:
            return JsonResponse({"message":str(i)})
        except Exception as e:
            return JsonResponse({"message":str(e)})
        
        return JsonResponse({"message":"Comment updated successfully"}, status=status.HTTP_200_OK)  

    def delete(self, request):
        try:
            commentInstance = Comment.objects.get(pk=request.GET.get('commentID'))
            issueInstance = commentInstance.issue
            sprintInstance = commentInstance.sprint
            if issueInstance:
                projectInstance = issueInstance.project
            if sprintInstance:
                projectInstance = sprintInstance.project
            file_paths = commentInstance.attachment

            if file_paths:
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        os.remove(file_path)
            if issueInstance:
                directory_path = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
            if sprintInstance:
                directory_path = os.path.join('media', 'uploads', 'Development', 'client', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}"))
            if os.path.exists(directory_path):
                if not os.listdir(directory_path):
                    os.rmdir(directory_path)
                else:
                    pass
            
            commentInstance.delete()

        except IndentationError as i:
            return JsonResponse({"message":str(i)})
        except Exception as e:
            return JsonResponse({"message":str(e)})
        
        return JsonResponse({"message":"Comment deleted successfully"})
    
class DownloadCommentsAttachments(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, CustomSessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            commentInstance = Comment.objects.get(pk=request.GET.get('commentID'))
            issueInstance = commentInstance.issue
            sprintInstance = commentInstance.sprint
            files = commentInstance.attachment

            if files:
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer,'w') as commentZip:
                    for file in files:
                        filename = file.split("\\")[-1]
                        commentZip.write(file, filename)
                response = HttpResponse(zip_buffer.getvalue(), content_type = 'application/zip')
                if issueInstance:
                    response['Content-Disposition'] = f'attachment; filename=comments_{issueInstance.key}_attachments.zip'
                if sprintInstance:
                    response['Content-Disposition'] = f'attachment; filename=comments_{sprintInstance.key}_attachments.zip'

            else:
                response = JsonResponse({"message":"No files found for the specified criteria"}, status=status.HTTP_204_NO_CONTENT)

        except IntegrityError as i:
            response = JsonResponse({"message":str(i)})

        except Exception as e:
            response = JsonResponse({"message":str(e)})
        return response

