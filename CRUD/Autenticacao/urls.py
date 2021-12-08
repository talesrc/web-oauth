from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = {
    #path('', view, name=""),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'autenticacao/login.html'
    ), name="login"),

}