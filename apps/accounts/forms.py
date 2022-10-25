from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label="Usuário", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Insira o usuário...', 
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Insira a senha...',
    }))