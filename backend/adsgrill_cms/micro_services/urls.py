from django.urls import path, re_path
from micro_services.users_management import users, roles
from micro_services.leads import leads
from micro_services.sales import sales

urlpatterns = [
    path("users/", users.UsersView.as_view()),
    path("roles/", roles.RolesView.as_view()),
    path("leads/", leads.LeadView.as_view()),
    path("leadinfo/", leads.LeadInfo.as_view()),
    path("leadExcelFormat/", leads.LeadExcelDownload.as_view()),
    path("sales/", sales.SalesView.as_view()),
]