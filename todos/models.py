from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )

    start = models.DateTimeField(
        auto_now_add = True,
        null = False,
        blank = False
    )

    deadline = models.DateField(
        null = False,                 
        blank = False
    )

    end = models.DateField(
        null = True,
        blank = True
    )
    


