from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()#Query a realizar
    permission_classes = [permissions.AllowAny]#Permisos de quien puede consultar
    serializer_class = ProjectSerializer#Que serializer va a estar usando estos datos, en que lo va a convertir.