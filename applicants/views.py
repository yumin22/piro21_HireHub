from django.shortcuts import render, redirect, get_object_or_404
from .models import Application, Answer
from accounts.models import Interviewer

# Create your views here.
def interview(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/interview.html", ctx)

def document(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/document.html", ctx)

def profile(request, pk):
    applicant = get_object_or_404(Application, pk=pk)
    answers = Answer.objects.filter(application=applicant)
    ctx = {
        'applicant': applicant,
        'answers': answers,
    }
    return render(request, 'applicant/profile.html', ctx)
