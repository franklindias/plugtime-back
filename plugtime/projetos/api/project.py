from rest_framework import generics
from django_filters import rest_framework as filters

from plugtime.projetos.models import Project
from plugtime.projetos.serializers.project import ProjectSerializer

class ProjectFilter(filters.FilterSet):
    title_contains = filters.CharFilter(field_name="title", lookup_expr='contains')

    class Meta:
        model = Project
        fields = ('title', 'description', 'estimated_time', 'time_value', 'title_contains')


class ProjectListCreate(generics.ListCreateAPIView):
    """
    get:
    Retorna uma lista com todos os Projetos existentes.

    post:
    Cria uma nova instacia de Projeto.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    ordering_fields = ('title', 'description', 'estimated_time', 'time_value', )
    search_fields = ('title', 'description')


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
