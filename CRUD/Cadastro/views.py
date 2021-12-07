from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class CadastroView(TemplateView):
    template_name = 'Cadastro/form.html'
