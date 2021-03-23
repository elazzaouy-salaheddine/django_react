from django.contrib import admin

# Register your models here.
from .models import Gte_Table_Comercial,Gte_Observations


class Gte_Table_Comercial_Admin(admin.ModelAdmin):
    list_display = ('project','project_booking','client','validite')
    list_filter = ('validite','category')



admin.site.register(Gte_Table_Comercial,Gte_Table_Comercial_Admin)

admin.site.register(Gte_Observations)