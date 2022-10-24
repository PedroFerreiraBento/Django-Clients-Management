from http import client
from rest_framework import serializers
from client.models import Client, RelatedCNPJ

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RelatedCNPJSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedCNPJ
        fields = '__all__'