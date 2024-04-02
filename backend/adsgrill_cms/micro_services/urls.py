from django.urls import path, re_path
from micro_services.users_management import users, roles
from micro_services.leads import leads
from micro_services.sales import sales
from micro_services.development import client, projects, sprints ,issues, comments,worklog


urlpatterns = [
    path("users/", users.UsersView.as_view()),
    path("roles/", roles.RolesView.as_view()),
    path("leads/", leads.LeadView.as_view()),
    path("leadinfo/", leads.LeadInfo.as_view()),
    path("leadExcelFormat/", leads.LeadExcelDownload.as_view()),
    path("sales/", sales.SalesView.as_view()),
    path("sales/getAllEmployees",sales.getAllSaleEmployees.as_view()),
    path("client/", projects.GetAllClients.as_view()),
    path("client/login/", client.ClientLogin.as_view()),
    path("development/projects", projects.ProjectView.as_view()),
    path("development/sprints", sprints.SprintView.as_view()),
    path("development/projects/download",projects.DownloadProjectAttchments.as_view()),
    path("development/issues",issues.IssueView.as_view()),
    path("development/linked_issues",issues.LinkedIssueView.as_view()),
    path("development/issues/download",issues.DownloadIssuesAttchments.as_view()),
    path("development/getProjectManagers", projects.GetProjectManagers.as_view()),
    path("development/getAssignees", projects.GetAllAssignees.as_view()),
    path("development/getTeamLeaders", projects.GetAllTeamLeaders.as_view()),
    path("development/comments", comments.CommentsView.as_view()),
    path("development/comments/download", comments.DownloadCommentsAttachments.as_view()),
    path("development/worklog",worklog.WorklogView.as_view()),
    path("development/worklog/download",worklog.DownloadWorklogAttachments.as_view()),
    path("development/issueMetaData",issues.IssueMetaData.as_view()),
    path("development/downloadUserWorkReport",issues.downloadUserWorkReport.as_view())
]