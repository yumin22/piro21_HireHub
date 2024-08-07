from django.shortcuts import render, redirect
from .models import Evaluation, EvaluationScore
from template.models import EvaluationTemplate, EvaluationQuestion
from applicants.models import Application
from accounts.models import Interviewer
from django.http import HttpResponseForbidden
from django.contrib import messages
# Create your views here.

def create_evaluation(req, pk):
    application = Application.objects.get(id=pk)
    interviewer = Interviewer.objects.get(id = req.user.id)
    template = EvaluationTemplate.objects.get(id=18)

    if not interviewer in application.interviewer.all():  # 배정된 면접관인지 확인
        return HttpResponseForbidden("배정된 면접관이 아닙니다.")
    
    existing_evaluation = Evaluation.objects.filter(application=application, interviewer=interviewer, template=template, is_submitted=True).first()
    if existing_evaluation:
        messages.error(req, '이미 제출한 평가입니다.')
        return render(req, 'evaluation_create.html', {
            'application': application,
            'template': template,
            'questions': template.questions.all()
        })
    
    if req.method == 'POST':
        evaluation = Evaluation.objects.create(
            application=application,
            interviewer=interviewer,
            template=template,
            comments=req.POST.get('comments', '')
        )

        for question in template.questions.all():
            score = req.POST.get(f'score_{question.id}')
            EvaluationScore.objects.create(
                evaluation=evaluation,
                question=question,
                score=score
            )
            
        evaluation.is_submitted = True
        evaluation.calculate_total_score()
        evaluation.save()
        messages.success(req, '평가가 성공적으로 제출되었습니다.')
        return redirect('applicants:profile', application.id)
    
    ctx = {
        'application': application,
        'template': template,
        'questions': template.questions.all()
    }
    return render(req, 'evaluation_create.html', ctx)

