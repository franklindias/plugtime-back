from django.urls import path

from plugtime.projetos.api import ProjectListCreate, ProjectRetrieveUpdateDestroy

app_name="projetos"

urlpatterns = [
    path('projects/', ProjectListCreate.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name="project-rud"),
]
