from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

# Create your views here.

class ClientesViewsSet(viewsets.ModelViewSet):
    '''Exibição de clientes'''
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
