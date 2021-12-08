from django.db.models import fields
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy

# Create your views here.
class UsuarioCreate(CreateView):
    template_name= "autenticacao/cadastroUser.html"
    form_class = UsuarioForm
    #fields = ['username', 'email', 'password']
    success_url = reverse_lazy('login')

#fhZTU63JYRc_gx8