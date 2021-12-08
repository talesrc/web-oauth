from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Livro, Local
from django.urls import reverse_lazy

################## CREAT ####################### 

class CadastroView(TemplateView):
    template_name = 'Cadastro/form.html'

class LocalCreat(CreateView):
    model = Local
    fields = ['codigo', 'descricao', 'corredor', 'estante']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('listar-local')

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
    success_url = reverse_lazy('listar-local')

class LivroUpdate(UpdateView):
    model = Livro
    fields = ['titulo', 'autor', 'ano', 'local']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')


################## DELETE ########################
class LocalDelete(DeleteView):
    model = Local
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('home')

class LivroDelete(DeleteView):
    model = Livro
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('listar-local')

################## READ ########################
class LocalList(ListView):
    model = Local
    template_name = 'Cadastro/listaLocal.html'

class LivroList(ListView):
    model = Livro
    template_name = 'Cadastro/listaLivro.html'
