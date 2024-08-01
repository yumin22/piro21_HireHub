from django.db import models
from accounts.models import Interviewer
# 지원서 템플릿을 저장해놓고
class ApplicationTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(Interviewer, on_delete=models.CASCADE)

# 여기서 질문을 추가할 수 있게 해놓음
class Question(models.Model):
    template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE, related_name='questions') # related_name쓰면 접근시 easy해서 쓴겨
    question_text = models.TextField()


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
    interview_date = models.DateTimeField(blank=True, null=True) 

class Answer(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #특정 질문에 대한 답변
    answer_text = models.TextField()

