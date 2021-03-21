from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.category
