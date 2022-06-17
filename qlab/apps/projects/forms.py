from django import forms

from .models import Post, Project


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "active",
        ]
        labels = {
            "title": "Project Title",
            "description": "Project Description",
            "active": "Active Project?"
        }


class PostForm(forms.Form):
    content = forms.CharField(max_length=5000, widget=forms.Textarea)
