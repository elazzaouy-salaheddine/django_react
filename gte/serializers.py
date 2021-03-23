from rest_framework import serializers
from .models import Gte_Table_Comercial


class GteProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gte_Table_Comercial
        fields = '__all__'
