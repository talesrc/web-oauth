from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView

urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    #path('endereco/', IndexView.as_view(), name='nome'),
]