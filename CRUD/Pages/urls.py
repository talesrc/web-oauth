from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView
from .views import ModeloView, SobreView

urlpatterns = [
    #Home - index.html
    path('', IndexView.as_view(), name='home'),  
    #path('', IndexView.as_view(), name='modelo'),
    #path('endereco/', IndexView.as_view(), name='nome'),

    #Sobre - sobre.html
    path('sobre/', SobreView.as_view(), name='sobre'),

    #Modelo - modelo.html
    path('modelo/',ModeloView.as_view(), name='modelo'),


]