from django.urls import path

from apps.modules.companies.views import get_companies

urlpatterns = [
    path('companies', get_companies),
]