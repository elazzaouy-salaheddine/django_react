from django.db import models
from client.models import Client

# Create your models here.

class Architect(models.Model):
    name = models.CharField(max_length=255)
    Rc = models.CharField(max_length=255, blank=True, null=True)
    ICE = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
