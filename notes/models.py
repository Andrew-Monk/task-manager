from django.db import models
from tasks.models import Task


# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=False)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="notes", null=True,
    )

    def __str__(self):
        return self.title
