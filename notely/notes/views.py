from rest_framework import permissions
from rest_framework import viewsets

from notely.notes.models import Category
from notely.notes.models import Note
from notely.notes.serializers import CategorySerializer
from notely.notes.serializers import NoteSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        note = serializer.save(author=self.request.user)
        collaborators = self.request.data.get("collaborators", [])
        categories = self.request.data.get("category_ids", [])
        note.collaborators.set(collaborators)
        note.category.set(categories)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
