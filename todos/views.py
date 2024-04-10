from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy
from todos.forms import InsertTodo

# Create your views here.
class TodoListView(ListView):
    template_name = "todos/home.html"
    model = Todo
    context_object_name = "todos"

class TodoCreateView(CreateView):
    template_name = "todos/create-todo.html"
    model = Todo
    form_class = InsertTodo
    success_url = reverse_lazy("home")

class TodoUpdateView(UpdateView):
    template_name = "todos/update-todo.html"
    model = Todo
    fields = '__all__'
    context_object_name = "todo"
    success_url = reverse_lazy("home")

class TodoDeleteView(DeleteView):
    template_name = "todos/delete-todo.html"
    model = Todo
    context_object_name = "todo"
    success_url = reverse_lazy("home")



