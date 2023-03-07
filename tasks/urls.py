from django.urls import path, include
from tasks.views import create_task, show_my_tasks


urlpatterns = [
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("projects/", include("projects.urls")),
    path("create/", create_task, name="create_task"),
]
