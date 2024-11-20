from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from notely.notes.models import Note
from notely.notes.serializers import NoteSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
