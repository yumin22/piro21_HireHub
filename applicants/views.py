from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Application, Answer, Comment
from accounts.models import Interviewer
from .forms import CommentForm

def interview(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/interview.html", ctx)

def document(request):
    applicants = Application.objects.all()
    ctx = {"applicants": applicants}
    return render(request, "applicant/document.html", ctx)

def search_applicant(request):
    search_txt = request.GET.get('search_txt')
    applicants = Application.objects.filter(name__icontains=search_txt)
    results = [{'id': applicant.id, 'name': applicant.name} for applicant in applicants]
    return JsonResponse(results, safe=False)

def profile(request, pk):
    applicant = get_object_or_404(Application, pk=pk)
    answers = Answer.objects.filter(application=applicant)
    ctx = {
        'applicant': applicant,
        'answers': answers,
    }
    return render(request, 'applicant/profile.html', ctx)

def comment(request, pk):
    applicant = get_object_or_404(Application, pk=pk)
    answers = Answer.objects.filter(application=applicant)
    comments = Comment.objects.filter(application=applicant).order_by('created_at')
    form = CommentForm()
    
    if request.method == 'POST':
        interviewer = get_object_or_404(Interviewer, email=request.user.email)  # 인터뷰어 객체 가져오기
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.application = applicant
            comment.interviewer = interviewer
            comment.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX 요청 확인
                return JsonResponse({
                    'success': True,
                    'comment': {
                        'text': comment.text,
                        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                        'interviewer': interviewer.email  # 인터뷰어 이메일 반환
                    }
                })
            else:
                return redirect('applicants:comment', pk=pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX 요청 확인
                return JsonResponse({'success': False, 'error': 'Invalid form submission', 'form_errors': form.errors.as_json()})
    
    ctx = {
        'applicant': applicant,
        'answers': answers,
        'comments': comments,
        'form': form,
    }
    return render(request, 'applicant/comments.html', ctx)
