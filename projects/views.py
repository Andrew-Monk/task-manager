from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects': projects
    }
    return render(request, 'projects/list_project.html', context)
