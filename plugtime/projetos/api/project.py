from rest_framework import generics

from plugtime.projetos.models import Project
from plugtime.projetos.serializers.project import ProjectSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
