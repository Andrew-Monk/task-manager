from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def list_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects': projects,
    }
    return render(request, 'projects/list_project.html', context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = project.tasks.all()
    context = {
        'project': project,
        'tasks': tasks,
    }
    return render(request, 'projects/show_project.html', context)
