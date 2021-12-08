from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Atividade, Disciplina
from django.urls import reverse_lazy

# Create your views here.

class CadastroView(TemplateView):
    template_name = 'Cadastro/form.html'

class DisciplinaCreat(CreateView):
    model = Disciplina
    fields = ['nome', 'descricao']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')

class AtividadeCreat(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'disciplina']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')