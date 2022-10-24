from django.urls import path

from .views import ClientListView, ClientUpdateView, ClientDashboardView

urlpatterns = [
    path('dashboard', ClientDashboardView.as_view(), name='client-dashboard'),
    path('list', ClientListView.as_view(), name='client-list'),
    path('<pk>/update', ClientUpdateView.as_view(), name='client-update')
]