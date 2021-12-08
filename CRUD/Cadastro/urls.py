from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CadastroView
from .views import LivroCreat, LocalCreat
from .views import LivroUpdate, LocalUpdate
from .views import LivroDelete, LocalDelete
from .views import LivroList, LocalList

urlpatterns = [
    #CREAT - form.html 
    path('cadastro/', CadastroView.as_view(), name='cadastro'),  
    path('cadastro/local/', LocalCreat.as_view(), name='cadastro-local'),
    path('cadastro/livro/', LivroCreat.as_view(), name='cadastro-livro'),

    #UPDATE
    path('editar/local/<str:pk>/', LocalUpdate.as_view(), name='editar-local'),
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar-livro'),

    #DELETE
    path('excluir/local/<str:pk>/', LocalDelete.as_view(), name='excluir-local'),
    path('excluir/livro/<int:pk>/', LivroDelete.as_view(), name='excluir-livro'),

    #READ
    path('listar/local/', LocalList.as_view(), name='listar-local'),
    path('listar/livro/', LivroList.as_view(), name='listar-livro'),

]