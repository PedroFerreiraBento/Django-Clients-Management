from django.contrib import admin

from .models import Company, RelatedCNPJ

admin.site.register(Company)
admin.site.register(RelatedCNPJ)