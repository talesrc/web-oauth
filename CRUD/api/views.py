from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework.views import APIView

from .serializers import LivroSerializer
from Cadastro.models import Livro

from rest_framework import generics
from rest_framework import mixins

class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Livro.objects.all()
        post = qs.first()
        #serializer = LivroSerializer(qs, many=True)  
        serializer = LivroSerializer(post)      
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LivroView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin, 
    generics.GenericAPIView):
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LivroCreateView(
    mixins.ListModelMixin, 
    generics.CreateAPIView):
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)