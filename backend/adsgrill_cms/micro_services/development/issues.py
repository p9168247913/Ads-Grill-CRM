from app.models import Users,Project,Sprint,Issue,LinkedIssue
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.db.models import ObjectDoesNotExist
from django.db import transaction
import os
from django.utils import timezone


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

            if Issue.objects.filter(title=title, project=project_id).exists():
                return JsonResponse({"message": "Issue with this title already exists"})

            with transaction.atomic():
                project_instance = Project.objects.get(pk=project_id)
                sprint_instance = Sprint.objects.get(pk=sprint_id)
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
                if assignee_ids or parent_issue_ids:
                    assignee_ids=assignee_ids.split(',')
                    for assignee_id in assignee_ids:
                        assignee=Users.objects.get(pk=assignee_id)
                        issue_instance.assignee.add(assignee)
                    
                    parent_issue_ids=parent_issue_ids.split(',')    
                    for parent_issue_id in parent_issue_ids:
                        parent_issue=Issue.objects.get(pk=parent_issue_id)
                        issue_instance.parent_issue.add(parent_issue)
                
                attachment_file_names = []
                for attachment in attachments:
                    subdirectory = os.path.join('media', 'uploads', 'Development', 'issues', str(f"{project_instance.key}_{sprint_instance.key}_{issue_instance.title}"))
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)
                    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
                    unique_filename = f"{timestamp}_{attachment.name}"
                    attachment_path = os.path.join(subdirectory, unique_filename)
                    with open(attachment_path, 'wb') as destination:
                        for chunk in attachment.chunks():
                            destination.write(chunk)

                    attachment_file_names.append(attachment_path)

                issue_instance.attachments = attachment_file_names
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