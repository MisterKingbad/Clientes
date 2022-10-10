from ast import Str
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    '''Serializador de clientes'''
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF deve ter 11 dígitos"})
    
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Nome deve conter apenas letras"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"RG deve ter 9 dígitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"Celular deve ter no máximo 11 dígitos"})
        return data
    
