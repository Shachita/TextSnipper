from django.db import models
from django.db.models.base import Model


# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    creator = models.BooleanField(default = True)



