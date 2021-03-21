from rest_framework import serializers
from .models import Architect


class ArchitectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architect
        fields = '__all__'
