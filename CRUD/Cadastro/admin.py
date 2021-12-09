from django.contrib import admin

#Importar as classes
from .models import Local, Livro

# Register your models here.
admin.site.register(Local)
admin.site.register(Livro)
