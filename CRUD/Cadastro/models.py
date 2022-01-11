from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Local(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Código")
    descricao = models.CharField(max_length=50, verbose_name="Gênero")
    corredor = models.IntegerField()
    estante = models.IntegerField()

    def __str__(self):
        return "{} - {}, {} ({})".format(self.codigo, self.descricao, self.corredor, self.estante)

class Livro(models.Model):
    #numero = models.IntegerField(verbose_name="Número")
    #descricao = models.CharField(max_length=150, verbose_name="Descrição")
    #pontos = models.DecimalField(decimal_places=1, max_digits=4)
    #detalhes = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=80, verbose_name="Título")
    autor = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return "{} - {}, {} ({})".format(self.titulo, self.autor, self.ano, self.local.codigo)

class Artigo(models.Model):
    titulo = models.CharField(max_length=80, verbose_name="Título")
    autor = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    ano = models.IntegerField()

    def __str__(self):
        return "{} - {}, {} ({})".format(self.titulo, self.autor, self.descricao, self.ano)

class Computer(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Código")
    data = models.DateField()
    horario = models.TimeField()
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=6, verbose_name="Matrícula")

    def __str__(self):
        return "{}, {} - {}, {} ({})".format(self.codigo, self.data, self.horario, self.nome, self.matricula)