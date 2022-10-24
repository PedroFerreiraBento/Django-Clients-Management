from django.db import models


class Client(models.Model):
    active = models.BooleanField("Ativo")
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", null=True, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", null=True, auto_now=True)

    def __str__(self):
        return self.name


class ClientHistory(models.Model):
    active = models.BooleanField("Ativo")
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", null=True, auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "client_client_history"


class RelatedCNPJ(models.Model):
    active = models.BooleanField("Ativo")
    cnpj = models.CharField("CNPJ", max_length=18)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", null=True, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", null=True, auto_now=True)

    def __str__(self):
        return self.cnpj


class RelatedCNPJHistory(models.Model):
    active = models.BooleanField("Ativo")
    cnpj = models.CharField("CNPJ", max_length=18)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField("Nome", max_length=255)
    created_at = models.DateTimeField("Criado em", null=True, auto_now_add=True)
    relatedcnpj = models.ForeignKey(RelatedCNPJ, on_delete=models.CASCADE)

    def __str__(self):
        return self.cnpj

    class Meta:
        db_table = "client_relatedcnpj_history"