from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project#Modelo al que pertenece el serializer
        fields = ('id', 'title', 'description', 'technology', 'created_date')#Campos que van a ser consultados (Tupla)
        read_only_fields = ('created_date', )#Campos de solo lectura (Tupla)