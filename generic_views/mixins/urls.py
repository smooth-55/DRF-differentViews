from django.urls import path

from .mixinViews import (
    TodoListMixin,
    TodoCreateMixin,
    TodoRetriveMixin,
    TodoPutMixin,
    TodoDeleteMixin,
    home,
)


urlpatterns = [
    path("list/", TodoListMixin.as_view(), name="get"),
    path("create/", TodoCreateMixin.as_view(), name="post"),
    path("retrive<int:pk>/", TodoRetriveMixin.as_view(), name="retrieve"),
    path("delete<int:pk>/", TodoDeleteMixin.as_view(), name="destroy"),
    path("update<int:pk>/", TodoPutMixin.as_view(), name="put"),
]