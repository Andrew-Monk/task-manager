from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm, FeedbackForm

# Create your views here.


@login_required
def list_project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list_project.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, pk=id)
    tasks = project.tasks.all()
    context = {
        "project": project,
        "tasks": tasks,
    }
    return render(request, "projects/show_project.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)

def thank_you(request):
    return render(request, "projects/thank_you.html")

@login_required
def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form = FeedbackForm()
    context = {
        "form": form,
    }
    return render(request, "projects/send_feedback.html", context)
