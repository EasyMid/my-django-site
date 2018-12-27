from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Authors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Articles(models.Model):
    id_author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)