from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import NoteView

router = DefaultRouter()
router.register(r"notes", NoteView)

app_name = "notes"
urlpatterns = [
    path("", include(router.urls)),
]
