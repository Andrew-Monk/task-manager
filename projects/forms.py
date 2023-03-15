from django import forms
from projects.models import Project, Feedback


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
            'generalfb': 'If you have any feedback on our services, we would love to hear from you!',
            'promotion': 'Would you be interested in receiving newsletters about our product and other promotional deals?',
        }
