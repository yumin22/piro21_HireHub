from django.db import models
from accounts.models import Interviewer
from template.models import ApplicationTemplate, Question


class Application(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interview_in_progress', 'Interview In Progress'),
        ('interview_completed', 'Interview Completed'),
    ]

    template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    interview_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f'{self.name}'

class Answer(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #특정 질문에 대한 답변
    answer_text = models.TextField()

