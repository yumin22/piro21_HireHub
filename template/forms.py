from django import forms
from .models import ApplicationTemplate, Question

class ApplicationTemplateForm(forms.ModelForm):
    class Meta:
        model = ApplicationTemplate
        fields = ['name' , 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


