from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView
from .views import ModeloView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('', IndexView.as_view(), name='modelo'),
    #path('endereco/', IndexView.as_view(), name='nome'),
    path('modelo/',ModeloView.as_view(), name='modelo'),

]