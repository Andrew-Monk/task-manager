from django import forms
<<<<<<< HEAD
from projects.models import Project, Survey
=======
from projects.models import Project, Feedback
>>>>>>> d60cb2c8d28351eac8b4cd82d2329014e9c6dc38


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'email',
            'generalfb',
            'promotion',
        ]
        labels = {
            'name': 'Name',
            'email': 'Email',
            'generalfb': 'Feedback',
            'promotion': 'Would you be interested in receiving newsletters about our product and other promotional deals?',
        }
