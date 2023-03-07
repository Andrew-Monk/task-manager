from django.urls import path
from projects.views import list_project, show_project


urlpatterns = [
    path('<int:id>/', show_project, name='show_project'),
    path('', list_project, name='list_projects'),
]
