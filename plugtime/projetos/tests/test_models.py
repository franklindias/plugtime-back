from django.test import TestCase
from django.utils import timezone
from plugtime.projetos.models import Project, Event, Participant

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title="Projeto teste",
            description="Descrição teste", estimated_time=50, time_value=40.00)

    def test_project_creation(self):
        self.assertTrue(isinstance(self.project, Project))
        self.assertEqual(self.project.__str__(), self.project.title)

class EventTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title="Projeto teste",
            description="Descrição teste", estimated_time=50, time_value=40.00)
        self.participant = Participant.objects.create(
            role="Programador",
            project=self.project
            )
        self.event = Event.objects.create(
            start=timezone.now(),
            end=timezone.now(),
            duration=timezone.now()-timezone.now(),
            description="Descrição teste",
            project=self.project,
            participant=self.participant
            )

    def test_event_creation(self):
        self.assertTrue(isinstance(self.event, Event))
        self.assertTrue(isinstance(self.event.project, Project))
        self.assertTrue(isinstance(self.event.participant, Participant))
        self.assertEqual(self.event.__str__(), self.event.description)


class ParticipantTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title="Projeto teste",
        description="Descrição teste", estimated_time=50, time_value=40.00)
        self.participant = Participant.objects.create(
            role="Programador",
            project=self.project
            )

    def test_participant_creation(self):
        self.assertTrue(isinstance(self.participant, Participant))
        self.assertTrue(isinstance(self.participant.project, Project))
        self.assertEqual(self.participant.__str__(), self.participant.role)
