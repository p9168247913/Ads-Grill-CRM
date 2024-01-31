from app.models import Project, Issue, Users, Sprint, Comment, LinkedIssue
from rest_framework.views import APIView
from rest_framework import status
import os
from django.http import JsonResponse, HttpResponse
from django.db.utils import IntegrityError
from django.db import transaction
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from braces.views import CsrfExemptMixin
from io import BytesIO
import zipfile
import uuid

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return
    
class CommentsView(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            currentUser = request.user
            requestData = request.data
            issueID = requestData.get('issueID')
            issueInstance = Issue.objects.get(pk=issueID)
            assignee = issueInstance.assignee
            sprintInstance = issueInstance.sprint
            projectInstance = sprintInstance.project
            if assignee!=currentUser:
                return JsonResponse({"message":"You dont have access to comment on other's issues"})
            
            attachments = request.FILES.getlist('attachments', [])
            attachment_file_names = []
            subDirectory = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
            if not os.path.exists(subDirectory):
                os.makedirs(subDirectory)
            for attachment in attachments:
                file_extension = attachment.name.split('.')[-1]
                unique_id = str(uuid.uuid4().hex[:6])
                unique_filename = f"{unique_id}_{issueInstance.key}.{file_extension}"
                attachment_path = os.path.join(subDirectory, unique_filename)

                with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                attachment_file_names.append(attachment_path)
            with transaction.atomic():
                commentInstance = Comment.objects.create(
                        sprint = sprintInstance,
                        issue = issueInstance,
                        author = currentUser,
                        description = requestData.get('desc'),
                        attachment = attachment_file_names
                    )
                commentInstance.save()
        except IndentationError as i:
            return JsonResponse({"message":str(i)})
        except Exception as e:
            return JsonResponse({"message":str(e)})

        return JsonResponse({"message":"Comment added succussfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        try:
            issueInstance = Issue.objects.get(pk=request.data.get('issueID'))
            allComments = Comment.objects.filter(issue=issueInstance).order_by('-created_at')
            responseData = [{
                "commentID": comment.pk,
                "sprintID":comment.sprint.pk,
                "IssueID":comment.issue.pk,
                "author":{
                    "id":comment.author.pk,
                    "name":comment.author.name,
                    "type":comment.author_type
                },
                "description":comment.description,
                "attachments":comment.attachment
            }for comment in allComments]

        except Exception as e:
            return JsonResponse({"message":str(e)})
        return JsonResponse({"comments":responseData}, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            requestData = request.data
            currentUser = request.user
            commentInstance = Comment.objects.get(pk=requestData.get('id'))
            issueInstance = commentInstance.issue
            sprintInstance = commentInstance.sprint
            projectInstance = sprintInstance.project

            if commentInstance.issue.assignee != currentUser:
                return JsonResponse({"message":"You dont have access to make changes in comment on other's issues"})
            attachments = request.FILES.getlist('attachments')

            subDirectory = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
            if not os.path.exists(subDirectory):
                os.makedirs(subDirectory)
            attachment_file_names = []
            for attachment in attachments:
                file_extension = attachment.name.split('.')[-1]
                unique_id = str(uuid.uuid4().hex[:6])
                unique_filename = f"{unique_id}_{issueInstance.key}.{file_extension}"
                attachment_path = os.path.join(subDirectory, unique_filename)

                with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                attachment_file_names.append(attachment_path)
            with transaction.atomic():
                commentInstance.description = requestData.get('desc'),
                commentInstance.attachment.extend(attachment_file_names)
                commentInstance.save()

        except IntegrityError as i:
            return JsonResponse({"message":str(i)})
        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse({"message":str(e)})
        
        return JsonResponse({"message":"Comment updated successfully"}, status=status.HTTP_200_OK)  

    def delete(self, request):
        try:
            commentInstance = Comment.objects.get(pk=request.GET.get('id'))
            issueInstance = commentInstance.issue
            sprintInstance = commentInstance.sprint
            projectInstance = sprintInstance.project
            file_paths = commentInstance.attachment

            if file_paths:
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        os.remove(file_path)

            directory_path = os.path.join('media', 'uploads', 'Development', 'comments', str(f"{projectInstance.key}_{sprintInstance.key}_{issueInstance.key}"))
            if os.path.exists(directory_path):
                os.rmdir(directory_path)
            
            commentInstance.delete()

        except IndentationError as i:
            return JsonResponse({"message":str(i)})
        except Exception as e:
            return JsonResponse({"message":str(e)})
        
        return JsonResponse({"message":"Comment deleted successfully"})
    
class DownloadCommentsAttachments(CsrfExemptMixin, APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            commentInstance = Comment.objects.get(pk=request.GET.get('id'))
            issueInstance = commentInstance.issue
            files = commentInstance.attachment

            if files:
                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer,'w') as commentZip:
                    for file in files:
                        filename = file.split("\\")[-1]
                        commentZip.write(file, filename)
                response = HttpResponse(zip_buffer.getvalue(), content_type = 'application/zip')
                response['Content-Disposition'] = f'attachment; filename=comments_{issueInstance.key}_attachments.zip'

            else:
                response = JsonResponse({"message":"No files found for the specified criteria"}, status=status.HTTP_204_NO_CONTENT)

        except IntegrityError as i:
            import traceback
            traceback.print_exc()
            response = JsonResponse({"message":str(i)})

        except Exception as e:
            import traceback
            traceback.print_exc()
            response = JsonResponse({"message":str(e)})
        return response

