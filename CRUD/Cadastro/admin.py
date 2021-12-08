from django.contrib import admin

#Importar as classes
from .models import Disciplina, Atividade

# Register your models here.
admin.site.register(Disciplina)
admin.site.register(Atividade)