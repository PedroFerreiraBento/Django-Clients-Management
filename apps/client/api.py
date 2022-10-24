from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from client.models import Client, RelatedCNPJ
from client.serializer import ClientSerializer, RelatedCNPJSerializer

class RelatedCNPJViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing clients related CNPJs.
    """
    queryset = RelatedCNPJ.objects.all()
    serializer_class = RelatedCNPJSerializer
    permission_classes = [AllowAny]


class ClientViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['GET'], name='Get Related CNPJs')
    def related_cnpjs(self, request, pk=None):
        queryset = self.queryset.get(id=pk).relatedcnpj_set.all()
        serializer = RelatedCNPJSerializer(queryset, many=True)
        return Response(serializer.data)