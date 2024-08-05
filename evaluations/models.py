from django.db import models
from accounts.models import Interviewer
from applicants.models import Application
from template.models import EvaluationTemplate, EvaluationQuestion
# Create your models here.
class Evaluation(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='evaluations')
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    template = models.ForeignKey(EvaluationTemplate, on_delete=models.CASCADE, default=1)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total_score(self):
        self.total_score = sum(score.score for score in self.scores.all())
        self.save()

class EvaluationScore(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='scores')
    question = models.ForeignKey(EvaluationQuestion, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)