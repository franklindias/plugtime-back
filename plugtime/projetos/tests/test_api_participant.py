import json

from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status

from plugtime.projetos.models import Participant
from plugtime.projetos.models import Project
from plugtime.projetos.serializers.participant import ParticipantSerializer

class ParticipantTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(title="Projeto teste",
                                        description="Descrição teste",
                                        estimated_time=50,
                                        time_value=40.00
                                        )
        self.data_valid = {
                'project':self.project.pk,
                'role':"Programador",
                }
        self.data_invalid = {
                'project':self.project.pk,
                'role':"",
                }

    def create_valid_participant(self):
        return self.client.post(
            reverse('project:participants'),
            data=json.dumps(self.data_valid),
            content_type='application/json'
        )

    def create_invalid_participant(self):
        return self.client.post(
            reverse('project:participants'),
            data=json.dumps(self.data_invalid),
            content_type='application/json'
        )

    def test_create_valid_participant(self):
        response = self.create_valid_participant()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Participant.objects.count(), 1)
        self.assertEqual(Participant.objects.get().role, "Programador")

    def test_create_invalid_participant(self):
          response = self.create_invalid_participant()
          self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_participants(self):
      self.create_valid_participant()
      response = self.client.get(reverse('project:participants'))
      participants = Participant.objects.all()
      serializer = ParticipantSerializer(participants, many=True)
      self.assertEqual(response.data, serializer.data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_valid_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.put(
          reverse('project:participants-rud', kwargs={'pk':participant_object.pk}),
          data=json.dumps(self.data_valid),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.put(
          reverse('project:participants-rud', kwargs={'pk':participant_object.pk}),
          data=json.dumps(self.data_invalid),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.delete(
          reverse('project:participants-rud', kwargs={'pk':participant_object.pk}),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.delete(
          reverse('project:participants-rud', kwargs={'pk':2}),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.get(
          reverse('project:participants-rud', kwargs={'pk':participant_object.pk}),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      serializer = ParticipantSerializer(participant_object, many=False)
      self.assertEqual(response.data, serializer.data)

    def test_retrieve_invalid_participant(self):
      self.create_valid_participant()
      participant_object = Participant.objects.get()
      response = self.client.get(
          reverse('project:participants-rud', kwargs={'pk':2}),
          content_type='application/json'
      )
      self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
