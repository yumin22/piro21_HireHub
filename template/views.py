from django.shortcuts import render, redirect
from .models import ApplicationTemplate, Question
from .forms import ApplicationTemplateForm, QuestionForm
from django.forms import modelformset_factory
from django.views import View
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy


# Create your views here.
class TemplateListView(View):
    def get(self, req):
        template = ApplicationTemplate.objects.all()
        return render(req, 'template_list.html', {'template': template})
    
class ApplicationTemplateCreateView(View):
    def get(self, req):
        template_form = ApplicationTemplateForm()
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
        formset = QuestionFormSet(queryset=Question.objects.none())
        return render(req, 'apply_create.html', {
            'template_form' : template_form,
            'formset' : formset
        })
    
    def post(self, req):
        template_form = ApplicationTemplateForm(req.POST)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
        formset = QuestionFormSet(req.POST, queryset=Question.objects.none())

        if template_form.is_valid():
            template = template_form.save(commit=False)
            template.created_by = req.user
            template.save()

        if formset.is_valid():
            formset_questions = formset.save(commit=False)
            for question in formset_questions:
                question.template = template
                question.save()

            return JsonResponse({'success': True, 'redirect': reverse('template:template_list')})
        else:
            return JsonResponse({'success': False, 'errors': template_form.errors}, status=400)
    
class TemplateDetailView(View):
    def get(self, req, pk):
        template = ApplicationTemplate.objects.get(pk=pk)
        questions = template.questions.all()
        return render(req, 'template_detail.html', {'template': template, 'questions':questions})

class TemplateUpdateView(View):
    def get(self, request, pk):
        template = ApplicationTemplate.objects.get(pk=pk)
        template_form = ApplicationTemplateForm(instance=template)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
        formset = QuestionFormSet(queryset=template.questions.all())
        return render(request, 'apply_update.html', {
            'template_form': template_form,
            'formset': formset,
            'template': template
        })

    def post(self, request, pk):
        template = ApplicationTemplate.objects.get(pk=pk)
        template_form = ApplicationTemplateForm(request.POST, instance=template)
        QuestionFormSet = modelformset_factory(Question, form=QuestionForm, extra=0)
        formset = QuestionFormSet(request.POST, queryset=template.questions.all())

        if template_form.is_valid() and formset.is_valid():
            template = template_form.save(commit=False)
            template.created_by = request.user
            template.save()
            formset.instance = template
            formset.save()

            # 동적으로 추가된 질문들 처리
            self._save_dynamic_questions(request, template)

            return JsonResponse({'success': True, 'redirect': reverse('template:template_detail', kwargs={'pk': template.pk})})
        else:
            return JsonResponse({'success': False, 'errors': {**template_form.errors, **formset.errors}}, status=400)

    def _save_dynamic_questions(self, request, template):
        questions = [v for k, v in request.POST.items() if k.startswith('questions[')]
        for question_text in questions:
            Question.objects.create(template=template, question_text=question_text)

class TemplateDeleteView(DeleteView):
    model = ApplicationTemplate
    success_url = reverse_lazy('template:template_list')
    template_name = 'apply_delete.html'

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if request.is_ajax():
            return JsonResponse({'success': True, 'redirect': self.success_url})
        else:
            return response