from django.db import models
from accounts.models import Interviewer
from applicants.models import Application

# Create your models here.
class Evaluation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='evaluations')
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
