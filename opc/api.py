from .models import Opc
from rest_framework import viewsets, permissions

from .serializers import OpcSerializer


class OpcViewSet(viewsets.ModelViewSet):
    queryset = Opc.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OpcSerializer
