from django.db import models


class Company(models.Model):
    active = models.BooleanField("Ativo")
    name = models.CharField("Nome", max_length=255)

    def __str__(self):
        return self.name


class RelatedCNPJ(models.Model):
    active = models.BooleanField("Ativo")
    cnpj = models.CharField("CNPJ", max_length=18)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=255)

    def __str__(self):
        return self.cnpj