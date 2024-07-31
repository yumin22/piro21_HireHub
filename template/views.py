from django.shortcuts import render, redirect
from .models import ApplicationTemplate, Question
from .forms import ApplicationTemplateForm, QuestionForm
from django.forms import modelformset_factory
from django.views import View
# Create your views here.
class ApplicationTemplateCreateView(View):
    def get(self, req):
        template_form = ApplicationTemplateForm()
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra = 1)
        formset = QuestionFormSet(queryset=Question.objects.none())
        return render(req, 'apply_create.html', {
            'template_form' : template_form,
            'formset' : formset
        })
    def post(self, req):
        template_form = ApplicationTemplateForm(req.POST)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra =1 )
        formset = QuestionFormSet(req.POST, queryset=Question.objects.none())

        if template_form.is_valid() and formset.is_valid():
            template = template_form.save(commit=False)
            template.created_by = req.user
            template.save()

            for form in formset:
                if form.cleaned_data.get('question_text'):
                    question = form.save(commit=False)
                    question.template = template
                    question.save()
            return redirect('')
        
        return render(req, 'apply_create.html', {
            'template_form': template_form,
            'formset': formset,
        })