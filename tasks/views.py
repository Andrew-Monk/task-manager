from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task
from django.http import HttpResponseRedirect
from notes.models import Note

# Create your views here


@login_required
def toggle_task_completion(request, task_id):
    task = Task.objects.get(id=task_id, assignee=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    if tasks.exists():
        return render(request, "tasks/show_my_tasks.html", context)
    else:
        context["no_tasks"] = True
        return render(request, "tasks/show_my_tasks.html", context)
