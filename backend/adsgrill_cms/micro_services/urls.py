from django.urls import path, re_path
from micro_services.users_management import users, roles
from micro_services.leads import leads
from micro_services.sales import sales
from micro_services.development import client, projects

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
    path("getLeadManagers/", projects.GetLeadManagers.as_view())
]