from .models import Nv_Table_Comercial
from rest_framework import viewsets, permissions

from .serializers import NovProjectsSerializer


class NovProjectsViewSet(viewsets.ModelViewSet):
    queryset = Nv_Table_Comercial.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NovProjectsSerializer
