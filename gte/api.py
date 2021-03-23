from .models import Gte_Table_Comercial
from rest_framework import viewsets, permissions

from .serializers import GteProjectsSerializer


class GteProjectsViewSet(viewsets.ModelViewSet):
    queryset = Gte_Table_Comercial.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GteProjectsSerializer
