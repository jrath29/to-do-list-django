from django import forms
from todos.models import Todo

class InsertTodo(forms.ModelForm):
    class Meta:
        model = Todo
        
        fields = [
        'title',
        'deadline',
        'end'
        ]