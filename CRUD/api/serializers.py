from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from rest_framework import serializers
from Cadastro.models import Livro

"""
from django import forms

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = {
            'titulo', 'autor'
        }
"""

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor']