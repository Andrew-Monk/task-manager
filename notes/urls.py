from django.urls import path

from notes.views import create_notes, edit_notes, show_notes

urlpatterns = [
    path("create/", create_notes, name="create_notes"),
    path("<int:id>/edit/", edit_notes, name="edit_notes"),
    path("<int:id>/", show_notes, name="show_notes"),
]
