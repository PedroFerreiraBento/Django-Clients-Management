from django.contrib import admin

from .models import Client, RelatedCNPJ

admin.site.register(Client)
admin.site.register(RelatedCNPJ)