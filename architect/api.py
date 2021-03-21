from .models import Architect
from rest_framework import viewsets, permissions

from .serializers import ArchitectSerializer


class ArchitectViewSet(viewsets.ModelViewSet):
    queryset = Architect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArchitectSerializer
