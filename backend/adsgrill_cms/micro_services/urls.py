from django.urls import path, re_path
from micro_services.users_management import users, roles
from micro_services.leads import leads
from micro_services.sales import sales
from micro_services.development import client, projects, sprints


urlpatterns = [
    path("users/", users.UsersView.as_view()),
    path("roles/", roles.RolesView.as_view()),
    path("leads/", leads.LeadView.as_view()),
    path("leadinfo/", leads.LeadInfo.as_view()),
    path("leadExcelFormat/", leads.LeadExcelDownload.as_view()),
    path("sales/", sales.SalesView.as_view()),
    path("client/", client.ClientView.as_view()),
    path("client/login/", client.ClientLogin.as_view()),
    path("development/projects", projects.ProjectView.as_view()),
    path("development/sprints", sprints.SprintView.as_view()),
    path("development/getProjectManagers", projects.GetProjectManagers.as_view()),
    path("development/getAssignees", projects.GetAllAssignees.as_view()),
    path("development/projects/download",projects.DownloadProjectAttchments.as_view())
]