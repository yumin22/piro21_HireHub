from django.shortcuts import render, redirect
from .models import ApplicationTemplate, Question
from .forms import ApplicationTemplateForm, QuestionForm
from django.forms import modelformset_factory
from django.views import View

# Create your views here.
class TemplateListView(View):
    def get(self, req):
        template = ApplicationTemplate.objects.all()
        return render(req, 'template_list.html', {'template': template})
    
class ApplicationTemplateCreateView(View):
    def get(self, req):
        template_form = ApplicationTemplateForm()
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm)
        formset = QuestionFormSet(queryset=Question.objects.none())
        return render(req, 'apply_create.html', {
            'template_form' : template_form,
            'formset' : formset
        })
    
    def post(self, req):
        template_form = ApplicationTemplateForm(req.POST)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm)
        formset = QuestionFormSet(req.POST, queryset=Question.objects.none())

        if template_form.is_valid() and formset.is_valid():
            template = template_form.save(commit=False)
            template.created_by = req.user
            template.save()

            questions = formset.save(commit=False)
            for question in questions:
                question.template = template
                question.save()
                
            return redirect('template:template_list')
        

        return render(req, 'apply_create.html', {
            'template_form': template_form,
            'formset': formset,
        })
    
class TemplateDetailView(View):
    def get(self, req, pk):
        template = ApplicationTemplate.objects.get(pk=pk)
        questions = template.questions.all()
        return render(req, 'template_detail.html', {'template': template, 'questions':questions})
