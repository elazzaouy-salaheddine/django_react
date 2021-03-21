from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('raison_social', 'email','phone_number','adress')

admin.site.register(Client,ClientAdmin)
