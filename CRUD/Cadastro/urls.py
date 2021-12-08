from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CadastroView
from .views import AtividadeCreat, DisciplinaCreat

urlpatterns = [
    #Cadastro - form.html
    path('cadastro/', CadastroView.as_view(), name='cadastro'),  
    path('cadastro/disciplina/', DisciplinaCreat.as_view(), name='cadastro-disciplina'),
    path('cadastro/atividade/', AtividadeCreat.as_view(), name='cadastro-atividade'),

]