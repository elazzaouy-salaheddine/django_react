from django.contrib import admin
from .models import Architect


# Register your models here.


class ArchitectAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']


admin.site.register(Architect, ArchitectAdmin)
