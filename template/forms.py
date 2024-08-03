from django import forms
from .models import ApplicationTemplate, Question

class ApplicationTemplateForm(forms.ModelForm):
    class Meta:
        model = ApplicationTemplate
        fields = ['name' , 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': '템플릿 제목을 입력하세요.'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': '(선택) 지원자들을 위한 지원서 작성 가이드를 입력해 주세요.'
            }),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']