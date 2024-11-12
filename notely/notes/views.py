from rest_framework import viewsets

from notely.notes.models import Note
from notely.notes.serializers import NoteSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = []

    def perform_create(self, serializer):
        note = serializer.save(author=self.request.user)
        collaborators = self.request.data.get("collaborators", [])
        categories = self.request.data.get("category_ids", [])
        note.collaborators.set(collaborators)
        note.category.set(categories)
