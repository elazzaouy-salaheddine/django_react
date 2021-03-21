from rest_framework import serializers
from .models import Opc


class OpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opc
        fields = '__all__'
