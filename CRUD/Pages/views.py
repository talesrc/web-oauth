#from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    #template_namme = index.html
    #template_name = 'Pages/index.html'
    template_name = 'Pages/modelo.html'
