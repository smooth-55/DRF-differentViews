from django.urls import path
from .genericModelMixins import TodoListCreate, TodoGetUpdateDelete

urlpatterns = [
    path("list-create/", TodoListCreate.as_view(), name="list-create"),
    path("get-update-delete/<int:pk>/", TodoGetUpdateDelete.as_view(), name="GUP"),
]
