from django.shortcuts import render, redirect
from .models import Evaluation, EvaluationScore
from template.models import EvaluationTemplate, EvaluationQuestion
from applicants.models import Application
from accounts.models import Interviewer
# Create your views here.
def create_evaluation(req, pk):
    application = Application.objects.get(id=pk)
    interviewer = Interviewer.objects.get(id = req.user.id)
    