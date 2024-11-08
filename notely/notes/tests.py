import pytest
from django.test import TransactionTestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from notely.notes.models import Category
from notely.notes.models import Note
from notely.notes.views import NoteView
from notely.users.models import User


@pytest.mark.django_db
class TestNoteView(TransactionTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",  # noqa: S106
        )
        self.category = Category.objects.create(name="Test Category")

    def test_create_note_authenticated(self):
        view = NoteView.as_view({"post": "create"})
        data = {
            "title": "Test Note",
            "content": "This is a test note.",
            "collaborators": [self.user.id],
            "category_ids": [self.category.id],
        }
        request = self.factory.post("/notes/", data, format="json")
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, 201)  # noqa: PT009
        self.assertTrue(  # noqa: PT009
            Note.objects.filter(author=self.user, title="Test Note").exists(),
        )

    def test_create_note_unauthenticated(self):
        view = NoteView.as_view({"post": "create"})
        data = {
            "title": "Test Note",
            "content": "This is a test note.",
            "collaborators": [self.user.id],
            "category_ids": [self.category.id],
        }
        request = self.factory.post("/notes/", data, format="json")
        response = view(request)
        self.assertEqual(response.status_code, 403)  # noqa: PT009
        self.assertFalse(Note.objects.filter(title="Test Note").exists())  # noqa: PT009
