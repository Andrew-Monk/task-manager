from django.urls import path
from projects.views import list_project, show_project, create_project


urlpatterns = [
    path('create/', create_project, name='create_project'),
    path('<int:id>/', show_project, name='show_project'),
    path('', list_project, name='list_projects'),
]
