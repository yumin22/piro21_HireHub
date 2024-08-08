from django import forms
from .models import ApplicationTemplate, ApplicationQuestion, Comment, individualQuestion, individualAnswer



class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)

    class Meta:
        model = ApplicationTemplate
        fields = ['name','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = individualQuestion
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = individualAnswer
        fields = ['text']