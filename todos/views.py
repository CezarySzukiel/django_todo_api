from django.shortcuts import render
from rest_framework import generics

from . import models, serializers


class DetailTodo(generics.RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
