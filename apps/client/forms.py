from django import forms
from client.models import Client

class ClientForm(forms.ModelForm):
    active = forms.TypedChoiceField(
        label="Ativo",
        widget=forms.Select(attrs={"class": "form-control"}), 
        coerce=lambda x: x =='True', 
        choices=((False, 'Não'), (True, 'Sim')))

    class Meta:
        model = Client
        fields = ("name", "active")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "active": forms.RadioSelect(attrs={"class": "form-control"})
        }