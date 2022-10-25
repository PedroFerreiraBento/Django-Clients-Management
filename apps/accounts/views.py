from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AuthenticatedView(View):
    pass

class LoginView(LoginView):
    authentication_form=UserLoginForm