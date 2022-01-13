"""CRUD URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.authtoken.views import obtain_auth_token

from api.views import LivroView, LivroCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('cadastros/', include('Pages.urls'))
    path('', include('Pages.urls')),
    path('', include('Cadastro.urls')),
    path('', include('Autenticacao.urls')),
    #path('api/', TestView.as_view(), name='test'),
    path('api/', LivroView.as_view(), name='test'),
    path('create/', LivroCreateView.as_view(), name='create'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include("social_django.urls"), name='social'),

]
