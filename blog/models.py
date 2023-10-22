from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default='acer')
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')
    date = models.DateField()

    def __str__(self):
        return self.title
