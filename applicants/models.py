from django.db import models
from accounts.models import Interviewer
from template.models import ApplicationTemplate, ApplicationQuestion
import datetime as dt

class Possible_date_list(models.Model):
    AMPM_CHOICES = [
        ('am', '오전'),
        ('pm', '오후'),
    ]
    # 면접일
    possible_date= models.DateField(blank=False, null=False)
    # 오전, 오후
    possible_ampm = models.CharField(max_length=50, choices=AMPM_CHOICES, blank=False, null=False)
    # 해당 타임(면접일/오전or오후) 최대 할당가능 면접 개수
    max_possible_interview = models.IntegerField("면접타임개수", default=0)
    
    def __str__(self):
        return f'{self.possible_date}, {self.possible_ampm}'

class Application(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interview_in_progress', 'Interview In Progress'),
        ('interview_completed', 'Interview Completed'),
    ]
    TIME_CHOICES = [(None, '------')]

    for x in range(9, 18):
        TIME_CHOICES.append((dt.time(hour=x), '{:02d}:00'.format(x)))
        TIME_CHOICES.append((dt.time(hour=x, minute=30), '{:02d}:30'.format(x)))

    template = models.ForeignKey(ApplicationTemplate, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    interviewer = models.ManyToManyField(Interviewer)
    possible_date = models.ManyToManyField(Possible_date_list, blank=True)
    interview_date = models.ForeignKey(Possible_date_list, on_delete=models.SET_NULL, blank=True, null=True, related_name='interview_date')
    interview_time = models.TimeField(choices=TIME_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f'{self.name}'

class Answer(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(ApplicationQuestion, on_delete=models.CASCADE) #특정 질문에 대한 답변
    answer_text = models.TextField()

