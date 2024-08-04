from django.shortcuts import render, redirect, get_object_or_404
from .models import Application, Answer
from accounts.models import Interviewer
from django.http import JsonResponse
from template.models import ApplicationTemplate, ApplicationQuestion
from .forms import ApplicationForm
from django.forms import modelformset_factory

# Create your views here.
def interview(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/interview.html", ctx)

def document(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/document.html", ctx)


def search_applicant(request):
    search_txt = request.GET.get('search_txt')
    applicants = Application.objects.filter(name__icontains=search_txt)
    results = [{'id': applicant.id, 'name': applicant.name} for applicant in applicants]
    return JsonResponse(results, safe=False)

def profile(request, pk):
    applicant = get_object_or_404(Application, pk=pk)
    answers = Answer.objects.filter(application=applicant)
    ctx = {
        'applicant': applicant,
        'answers': answers,
    }
    return render(request, 'applicant/profile.html', ctx)

def apply(request, pk):
    template = ApplicationTemplate.objects.get(id=pk)

    if request.method == 'POST':
        application = Application(
            template = template,
            name = request.POST['name'],
            phone_number = request.POST['phone_number'],
            school = request.POST['school'],
            major = request.POST['major'],
        )
        application.save()

        for question in template.questions.all():
            answer_text = request.POST.get(f'answer_{question.id}')
            Answer.objects.create(
                application = application,
                question = question,
                answer_text = answer_text
            )
        return redirect('accounts:initialApplicant')
        
    context = {
        'template': template,
    }
    return render(request, 'applicant/write_apply.html', context)