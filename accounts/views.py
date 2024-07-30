from django.shortcuts import render, redirect, get_object_or_404
from applicants.models import Application
from .models import Interviewer
# Create your views here.

def mainboard(request,pk):
    applicants = Application.objects.filter(interviewer=pk)
    # get_object_or_404(Application, interviewer=pk)
    ctx = {"applicants":applicants}
    return render(request, "mainboard.html", ctx)
