from django import forms
from .models import ApplicationTemplate, ApplicationQuestion, Comment



class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)

    class Meta:
        model = ApplicationTemplate
        fields = ['name','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']