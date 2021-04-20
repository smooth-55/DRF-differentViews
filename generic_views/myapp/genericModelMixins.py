from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework import mixins, generics


class TodoListCreate(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


# class TodoListCreate(generics.ListCreateAPIView):
#     queryset = TodoList.objects.all()
#     serializer_class = TodoListSerializer


# class TodoListCreate(generics.ListCreateAPIView):
#     queryset = TodoList.objects.all()
#     serializer_class = TodoListSerializer