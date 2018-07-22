import json

from django.urls import reverse
from django.test import TestCase, Client
from django.utils import timezone

from rest_framework import status

from plugtime.projetos.models import Project, Participant, Event

class EventTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(title="Projeto teste",
                                        description="Descrição teste",
                                        estimated_time=50,
                                        time_value=40.00
                                        )

        self.participant = Participant.objects.create(
                                        project=self.project,
                                        role="Programador"
                                        )
        self.data_valid = {
                'project': self.project.pk,
                'participant': self.participant.pk,                
                'start': str(timezone.now()),
                'end': str(timezone.now()),
                'duration': str(timezone.now()-timezone.now()),
                'description': "Descrição do evento",
                }
        self.data_invalid = {
                'project': self.project.pk,
                'participant': self.participant.pk,                
                'start': str(timezone.now()),
                'end': str(timezone.now()),
                'duration': str(timezone.now()-timezone.now()),
                'description': "",
                }
    
        self.response_valid_event = self.client.post(
                reverse('project:events'),
                data=json.dumps(self.data_valid),
                content_type='application/json'
        )
    
        self.response_invalid_event = self.client.post(
                reverse('project:events'),
                data=json.dumps(self.data_invalid),
                content_type='application/json'
        )

    def test_create_valid_event(self):
        self.assertEqual(self.response_valid_event.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().description, "Descrição do evento")

    def test_create_invalid_event(self):
          self.assertEqual(self.response_invalid_event.status_code, status.HTTP_400_BAD_REQUEST)