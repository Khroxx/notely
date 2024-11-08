from django.contrib import admin

from .models import Category
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("created_at", "updated_at", "author")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
