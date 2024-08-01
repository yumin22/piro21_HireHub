from django.shortcuts import render, redirect, get_object_or_404
from .models import Application
from accounts.models import Interviewer
from django.http import JsonResponse

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