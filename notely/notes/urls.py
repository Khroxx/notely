from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryView
from .views import NoteView

router = DefaultRouter()
router.register(r"notes", NoteView)
router.register(r"categories", CategoryView)

app_name = "notes"
urlpatterns = [
    path("", include(router.urls)),
]
