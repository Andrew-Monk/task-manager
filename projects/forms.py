from django import forms
from projects.models import Project, Survey


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            "name",
            "email",
            "feedback",
            "general_feedback",
        ]

        labels = {
            "general_feedback": "Would you like to receive promotional newsletter?",
        }
