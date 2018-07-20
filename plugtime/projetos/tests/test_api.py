import json

from django.urls import reverse
from django.test import TestCase, Client

from rest_framework import status

from plugtime.projetos.models import Project
from plugtime.projetos.serializers import ProjectSerializer


class ProjectTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.data_valid = {
                'title':"Projeto teste",
                'description':"Descrição teste",
                'estimated_time':50,
                'time_value':40.00
                }
        self.data_invalid = {
                'title':"",
                'description':"Descrição teste",
                'estimated_time':50,
                'time_value':40
                }


    def create_valid_project(self):
        return self.client.post(
            reverse('project:projects'),
            data=json.dumps(self.data_valid),
            content_type='application/json'
        )

    def create_invalid_project(self):
        return self.client.post(
            reverse('project:projects'),
            data=json.dumps(self.data_invalid),
            content_type='application/json'
        )


    def test_create_valid_project(self):
        response = self.create_valid_project()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().title, "Projeto teste")


    def test_create_invalid_project(self):
        response = self.create_invalid_project()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_projects(self):
        self.create_valid_project()
        response = self.client.get(reverse('project:projects'))
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_valid_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.put(
            reverse('project:project-rud', kwargs={'pk':project_object.pk}),
            data=json.dumps(self.data_valid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.put(
            reverse('project:project-rud', kwargs={'pk':project_object.pk}),
            data=json.dumps(self.data_invalid),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.delete(
            reverse('project:project-rud', kwargs={'pk':project_object.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.delete(
            reverse('project:project-rud', kwargs={'pk':2}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.get(
            reverse('project:project-rud', kwargs={'pk':project_object.pk}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], project_object.title)

    def test_retrieve_invalid_project(self):
        self.create_valid_project()
        project_object = Project.objects.get()
        response = self.client.get(
            reverse('project:project-rud', kwargs={'pk':2}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
