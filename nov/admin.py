from django.contrib import admin
from.models import Nv_Observations,Nv_Table_Comercial
# Register your models here.

class Nv_Table_Comercial_Admin(admin.ModelAdmin):
    list_display=('project','project_booking','lieu','client')
    list_filter =('lieu','archive',)


class Nv_Observation_Admin(admin.ModelAdmin):
    list_display = ('project','create_by','date_add')





admin.site.register(Nv_Table_Comercial,Nv_Table_Comercial_Admin)
admin.site.register(Nv_Observations,Nv_Observation_Admin)