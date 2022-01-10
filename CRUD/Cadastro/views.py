from django.db import models
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Livro, Local, Artigo, Computer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Teste de github

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
    success_url = reverse_lazy('listar-livro')

class ArtigoCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Artigo
    fields = ['titulo', 'autor', 'descricao', 'ano']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('listar-artigo')

class ComputerCreat(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Computer
    fields = ['codigo', 'data', 'horario', 'matricula']
    template_name = 'Cadastro/form.html'
    success_url = reverse_lazy('listar-computer')

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

class ComputerUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Computer
    fields = ['codigo', 'data', 'horario', 'nome', 'matricula']
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

class ComputerDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Computer
    template_name = 'Cadastro/excluir.html'
    success_url = reverse_lazy('home')

################## READ ########################
class LocalList(ListView):
    login_url = reverse_lazy('login')
    model = Local
    template_name = 'Cadastro/listaLocal.html'

class LivroList(ListView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = 'Cadastro/listaLivro.html'

class ArtigoList(ListView):
    login_url = reverse_lazy('login')
    model = Artigo
    template_name = 'Cadastro/listaTeses.html'

class ComputerList(ListView):
    login_url = reverse_lazy('login')
    model = Computer
    template_name = 'Cadastro/listaPC.html'

#class LivroList(ListView):
#    login_url = reverse_lazy('login')
#    model = Livro
#    template_name = 'Cadastro/livros.html'

#class ArtList(ListView):
#    login_url = reverse_lazy('login')
#    model = Artigo
#    template_name = 'Cadastro/artigos.html'