from django.urls import path
from notes.views import create_notes, edit_notes, show_notes

urlpatterns = [
    path("create/", create_notes, name="create_notes"),
    path("<str:task>/edit/", edit_notes, name="edit_notes"),
    path("<str:task>/", show_notes, name="show_notes"),
]
