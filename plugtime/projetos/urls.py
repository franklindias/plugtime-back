from django.urls import path

from plugtime.projetos.api.project import ProjectListCreate, ProjectRetrieveUpdateDestroy
from plugtime.projetos.api.participant import ParticipantListCreate, ParticipantRetrieveUpdateDestroy
from plugtime.projetos.api.event import EventListCreate, EventRetrieveUpdateDestroy

app_name="projetos"

urlpatterns = [
    path('projects/', ProjectListCreate.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name="projects-rud"),

    path('participants/', ParticipantListCreate.as_view(), name="participants"),
    path('participants/<int:pk>/', ParticipantRetrieveUpdateDestroy.as_view(), name="participants-rud"),

    path('events/', EventListCreate.as_view(), name="events"),
    path('events/<int:pk>/', EventRetrieveUpdateDestroy.as_view(), name="events-rud")
]
