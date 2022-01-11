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
            'local','titulo', 'autor','ano'
        }
"""

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['local','titulo', 'autor','ano']