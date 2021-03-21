from django.contrib import admin
from .models import Opc
# Register your models here.

class OpcAdmin(admin.ModelAdmin):
    list_display = ['raison_social','email','phone_number','adress']



admin.site.register(Opc,OpcAdmin)