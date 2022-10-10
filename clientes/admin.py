from django.contrib import admin
from clientes.models import Clientes
# Register your models here.

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone', 'data_criacao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    
admin.site.register(Clientes, Clientes)