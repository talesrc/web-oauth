from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Livro, Local
from django.urls import reverse_lazy

################## CREAT ####################### 

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

################## UPDATE ####################### 

class LocalUpdate(UpdateView):
    model = Local
    fields = ['codigo', 'descricao', 'corredor', 'estante']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')

class LivroUpdate(UpdateView):
    model = Livro
    fields = ['titulo', 'autor', 'ano', 'local']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')


################## DELETE ########################
class LocalDelete(DeleteView):
    model = Local
    template_name = 'Cadastro/tela-excluir.html'
    success_url = reverse_lazy('home')

class LivroDelete(DeleteView):
    model = Livro
    template_name = 'Cadastro/tela-excluir.html'
    success_url = reverse_lazy('home')
