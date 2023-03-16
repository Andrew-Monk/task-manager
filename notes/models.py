from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title
