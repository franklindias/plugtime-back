from django.urls import path

from plugtime.projetos.api.project import ProjectListCreate, ProjectRetrieveUpdateDestroy

app_name="projetos"

urlpatterns = [
    path('projects/', ProjectListCreate.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name="project-rud"),
]
