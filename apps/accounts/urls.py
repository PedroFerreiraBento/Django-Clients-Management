from django.urls import path
from accounts.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout')
]