from django.db import models
from accounts.models import Interviewer
# Create your models here.
class ApplicationTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(Interviewer, on_delete=models.CASCADE)

# 여기서 질문을 추가할 수 있게 해놓음
class Question(models.Model):
    template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE, related_name='questions') # related_name쓰면 접근시 easy해서 쓴겨
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class InterviewQuestionTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(Interviewer, on_delete=models.CASCADE)

class InterviewQuestion(models.Model):
    template = models.ForeignKey(InterviewQuestionTemplate, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_importance = models.IntegerField(default=1)
