from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CadastroView
from .views import LivroCreat, LocalCreat, ArtigoCreat, ComputerCreat
from .views import LivroUpdate, LocalUpdate, ArtigoUpdate, ComputerUpdate
from .views import LivroDelete, LocalDelete, ArtigoDelete, ComputerDelete
from .views import LivroList, LocalList, ArtigoList, ComputerList

urlpatterns = [
    #CREAT - form.html 
    path('cadastro/', CadastroView.as_view(), name='cadastro'),  
    path('cadastro/local/', LocalCreat.as_view(), name='cadastro-local'),
    path('cadastro/livro/', LivroCreat.as_view(), name='cadastro-livro'),
    path('cadastro/artigo/', ArtigoCreat.as_view(), name='cadastro-artigo'),
    path('cadastro/computer/', ComputerCreat.as_view(), name='cadastro-computer'),

    #UPDATE
    path('editar/local/<str:pk>/', LocalUpdate.as_view(), name='editar-local'),
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar-livro'),
    path('editar/artigo/<int:pk>/', ArtigoUpdate.as_view(), name='editar-artigo'),
    path('editar/computer/<str:pk>/', ComputerUpdate.as_view(), name='editar-computer'),



    #DELETE
    path('excluir/local/<str:pk>/', LocalDelete.as_view(), name='excluir-local'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),
    path('excluir/artigo/<int:pk>/', ArtigoDelete.as_view(), name='excluir-artigo'),
    path('excluir/computer/<str:pk>/', ComputerDelete.as_view(), name='excluir-computer'),


    #READ
    path('listar/local/', LocalList.as_view(), name='listar-local'),
    path('listar/livro/', LivroList.as_view(), name='listar-livro'),
    path('listar/artigo/', ArtigoList.as_view(), name='listar-artigo'),
    path('listar/computer/', ComputerList.as_view(), name='listar-computer'),


    #READ não autenticado
    #path('exibir/livro/', LivroList.as_view(), name='exibir-livro'),
    #path('exibir/artigo/', ArtigoList.as_view(), name='exibir-artigo'),


]