from django.urls import path
from contacts.views import list_contacts

urlpatterns = [
    path("", list_contacts, name="list_contacts")
]
