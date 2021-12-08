from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Livro, Local
from django.urls import reverse_lazy

# Create your views here.

class CadastroView(TemplateView):
    template_name = 'Cadastro/form.html'

class LocalCreat(CreateView):
    model = Local
    fields = ['codigo', 'descricao', 'corredor', 'estante']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')

class LivroCreat(CreateView):
    model = Livro
    fields = ['titulo', 'autor', 'ano', 'local']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')