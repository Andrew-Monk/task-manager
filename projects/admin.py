from django.contrib import admin
<<<<<<< HEAD
from projects.models import Project, Survey
=======
from projects.models import Project, Feedback
>>>>>>> d60cb2c8d28351eac8b4cd82d2329014e9c6dc38

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "generalfb",
        "promotion",
    )
