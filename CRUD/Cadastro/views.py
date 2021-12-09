from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Livro, Local, Artigo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

################## CREAT ####################### 

class CadastroView(TemplateView):
    template_name = 'Cadastro/form.html'

class LocalCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Local
    fields = ['codigo', 'descricao', 'corredor', 'estante']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('listar-local')

class LivroCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Livro
    fields = ['titulo', 'autor', 'ano', 'local']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('lista-livro')

class ArtigoCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Artigo
    fields = ['titulo', 'autor', 'descricao', 'ano']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('lista-artigo')

################## UPDATE ####################### 

class LocalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Local
    fields = ['codigo', 'descricao', 'corredor', 'estante']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('listar-local')

class LivroUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Livro
    fields = ['titulo', 'autor', 'ano', 'local']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')

class ArtigoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Artigo
    fields = ['titulo', 'autor', 'descricao', 'ano']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('home')

################## DELETE ########################
class LocalDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Local
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('home')

class LivroDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('listar-local')

class ArtigoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Artigo
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('home')

################## READ ########################
class LocalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Local
    template_name = 'Cadastro/listaLocal.html'

class LivroList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = 'Cadastro/listaLivro.html'

class ArtigoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Artigo
    template_name = 'Cadastro/listaTeses.html'
