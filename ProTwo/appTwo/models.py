from django.db import models
from django.db.models.base import Model

# Create your models here.
# we create tables in our data

class User(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    email=models.EmailField(max_length=256,unique=True)
