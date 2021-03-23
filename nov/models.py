from django.db import models
import datetime
from ckeditor.fields import RichTextField
from client.models import Client
from django.contrib.auth.models import User
from category.models import Category
from architect.models import Architect
from opc.models import Opc
# Create your models here.



def nv_id_generator():
  last_project = Nv_Table_Comercial.objects.all().last()
  if not last_project:
    return 'NV-' + str(datetime.date.today().year)  + '0000'

  booking_int = int(last_project.id)
  new_booking_int = booking_int + 1
  new_booking_id = 'NV-' + str(str(datetime.date.today().year)) +'-'+ str(new_booking_int).zfill(4)
  return new_booking_id


PROJET_CHOICES = (
        ('en cours', 'en cours'),
        ('envoyeé', 'envoyeé'),
        ('validé', 'validé'),
        ('Annuler', 'Annuler'),
    )


class Nv_Table_Comercial(models.Model):
    project_booking = models.CharField(max_length=20, default = nv_id_generator, editable=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    project_type = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.ForeignKey(User,related_name='project_manager_nov',on_delete=models.CASCADE)
    lieu = models.CharField(max_length=255, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    validite = models.CharField(max_length=20, choices=PROJET_CHOICES)
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    OPC = models.ForeignKey(Opc, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.project
    
class Nv_Observations(models.Model):
    project = models.ForeignKey(Nv_Table_Comercial, related_name='nv_observations_project', on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, related_name='nv_observations_creatore', on_delete=models.CASCADE)
    body = models.TextField()
    file_comment = models.FileField(null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_add']

    def __str__(self):
        return self.body

