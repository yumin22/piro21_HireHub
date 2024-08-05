from django import forms
from django.forms.models import inlineformset_factory
from .models import ApplicationTemplate, Question, Comment


QuestionFormSet = inlineformset_factory(
    ApplicationTemplate, 
    Question, 
    fields=('question_text',), 
    extra=1, 
    can_delete=True
)

class ApplicationForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)

    class Meta:
        model = ApplicationTemplate
        fields = ['name','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']