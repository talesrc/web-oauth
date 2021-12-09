from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CadastroView
from .views import LivroCreat, LocalCreat, ArtigoCreat
from .views import LivroUpdate, LocalUpdate, ArtigoUpdate
from .views import LivroDelete, LocalDelete, ArtigoDelete
from .views import LivroList, LocalList, ArtigoList

urlpatterns = [
    #CREAT - form.html 
    path('cadastro/', CadastroView.as_view(), name='cadastro'),  
    path('cadastro/local/', LocalCreat.as_view(), name='cadastro-local'),
    path('cadastro/livro/', LivroCreat.as_view(), name='cadastro-livro'),
    path('cadastro/artigo/', ArtigoCreat.as_view(), name='cadastro-artigo'),


    #UPDATE
    path('editar/local/<str:pk>/', LocalUpdate.as_view(), name='editar-local'),
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar-livro'),
    path('editar/artigo/<int:pk>/', ArtigoUpdate.as_view(), name='editar-artigo'),


    #DELETE
    path('excluir/local/<str:pk>/', LocalDelete.as_view(), name='excluir-local'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/artigo/<int:pk>/', ArtigoDelete.as_view(), name='excluir-artigo'),

    #READ
    path('listar/local/', LocalList.as_view(), name='listar-local'),
    path('listar/livro/', LivroList.as_view(), name='listar-livro'),
    path('listar/artigo/', ArtigoList.as_view(), name='listar-artigo'),

    #READ não autenticado
    path('exibir/livro/', LivroList.as_view(), name='exibir-livro'),
    path('exibir/artigo/', ArtigoList.as_view(), name='exibir-artigo'),


]