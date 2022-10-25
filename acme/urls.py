"""acme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.client.api import ClientViewSet, RelatedCNPJViewSet
from django.views.generic.base import RedirectView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'client', ClientViewSet, basename="api-client")
router.register(r'related_cnpj', RelatedCNPJViewSet, basename="api-related_cnpj")

urlpatterns = [
    path('', RedirectView.as_view(pattern_name = 'login'), name="admin"),
    path('admin/', admin.site.urls, name="admin"),
    # Custom accounts endpoints
    path("accounts/", include('accounts.urls'), name="accounts"),
    # Default accounts endpoints
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),
    path('api/', include(router.urls), name="api"),
    path('client/', include('client.urls'), name="client"),
]