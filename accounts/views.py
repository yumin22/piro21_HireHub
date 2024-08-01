from django.shortcuts import render, redirect, get_object_or_404
from applicants.models import Application
from .models import Interviewer
from django.db.models import Q
# Create your views here.

def mainboard(request,pk):
    applicants = Application.objects.filter(interviewer=pk)
    sort_applicants = Application.objects.filter(interviewer=pk)
    sort = request.GET.get('sort','')

    if sort == 'submitted':
        sort_applicants = sort_applicants.filter(status='submitted')
    elif sort == 'scheduled':
        sort_applicants = sort_applicants.filter(status='interview_scheduled')
    elif sort == 'in_progress':
        sort_applicants = sort_applicants.filter(status='interview_in_progress')
    elif sort == 'completed':
        sort_applicants = sort_applicants.filter(status='interview_completed')
    else:
        sort_applicants = sort_applicants

    interview_num = applicants.filter(~Q(status='submitted')).count()
    ctx = {"applicants":applicants, "sort_applicants":sort_applicants, "pk":pk, "interview_num": interview_num}
    return render(request, "mainboard.html", ctx)
