from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from notes.serializers import NoteSerializer
from notes.models import Note

class CreateListNotes(ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subject']
