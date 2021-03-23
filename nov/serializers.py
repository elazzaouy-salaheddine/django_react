from rest_framework import serializers
from .models import Nv_Table_Comercial


class NovProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nv_Table_Comercial
        fields = '__all__'
