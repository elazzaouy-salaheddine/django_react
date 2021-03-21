from django.db import models


# Create your models here.

class Opc(models.Model):
    raison_social = models.CharField(max_length=255)
    Rc = models.CharField(max_length=255,blank=True, null=True)
    ICE = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    phone_number = models.CharField(max_length=255,blank=True, null=True)
    adress = models.CharField(max_length=255,blank=True, null=True)
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.raison_social
    