from rest_framework import generics

from plugtime.projetos.models import Participant
from plugtime.projetos.serializers.participant import ParticipantSerializer

class ParticipantListCreate(generics.ListCreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
