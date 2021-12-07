from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CadastroView

urlpatterns = [
    #Cadastro - form.html
    path('cadastro/', CadastroView.as_view(), name='cadastro'),  
]