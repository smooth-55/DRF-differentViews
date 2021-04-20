from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


# Create your views here.


def home(request):
    return HttpResponse("<h3>Mixins rendered!</h3>")


class TodoListMixin(GenericAPIView, ListModelMixin):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TodoCreateMixin(GenericAPIView, CreateModelMixin):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TodoRetriveMixin(GenericAPIView, RetrieveModelMixin):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrive(request, *args, **kwargs)


class TodoPutMixin(GenericAPIView, UpdateModelMixin):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class TodoDeleteMixin(GenericAPIView, DestroyModelMixin):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
