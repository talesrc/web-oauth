#from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    #template_name = index.html
    template_name = 'Pages/index.html'
    #template_name = 'Pages/modelo.html'

class ModeloView(TemplateView):
    template_name = 'Pages/modelo.html'

class SobreView(TemplateView):
    template_name = 'Pages/sobre.html'