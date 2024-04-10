from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoListView.as_view(), name="home"),
    path("create/", TodoCreateView.as_view(), name="create_todo"),
    path("update/<pk>", TodoUpdateView.as_view(), name="update_todo"),
    path("delete/<pk>", TodoDeleteView.as_view(), name="delete_todo")
]
