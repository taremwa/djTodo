from django.db import models

# Create your models here.
from authentication.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title