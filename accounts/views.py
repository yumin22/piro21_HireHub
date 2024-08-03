from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from .models import Interviewer
from applicants.models import Application
from template.models import ApplicationTemplate
from .forms import SignupForm, LoginForm

# Create your views here.

def initial(request):
   template = ApplicationTemplate.objects.get(pk=1)
   context = {'template': template}
   return render(request, 'accounts/initial.html', context)

def signup(request):
   if request.method == 'GET':
      form = SignupForm()
      context = {'form': form}
      return render(request, 'accounts/signup.html', context)
   else:
      form = SignupForm(request.POST)
      if form.is_valid():
         interviewer = form.save(commit=False)
         interviewer.is_approved = False # 관리자의 승인이 필요하므로 비활성화
         interviewer.save()
         return render(request, 'accounts/signupcheck.html')
      else:
         context = {'form': form}
         return render(request, 'accounts/signup.html', context)

def signupCheck(request):
   return render(request, 'accounts/signupcheck.html')

def login(request):
   if request.method == 'POST':
      form = LoginForm(request, request.POST)
      if form.is_valid():
         email = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(request, username=email, password=password)
         if user is not None:
            if user.is_approved and user.is_active: # 관리자의 승인을 받았으며 활성화되었을 때
               auth_login(request, user)
               return redirect(reverse('accounts:mainboard', kwargs={'pk': user.pk})) # 로그인한 유저의 mainboard로 이동
            else:
               return render(request, 'accounts/requiredapproval.html')
         else:
            form.add_error(None, '이메일 또는 비밀번호가 잘못되었습니다.')
   else:
      form = LoginForm()

   context = {'form': form}
   return render(request, 'accounts/login.html', context)

def requiredApproval(request):
   return render(request, 'accounts/requiredapproval.html')

def logout(request):
   auth_logout(request)
   return redirect('accounts:initial')

def mainboard(request,pk):
   applicants = Application.objects.filter(interviewer=pk)
   sort_applicants = Application.objects.filter(interviewer=pk)
   sort = request.GET.get('sort','')

   if sort == 'submitted':
      sort_applicants = sort_applicants.filter(status='submitted')
   elif sort == 'scheduled':
      sort_applicants = sort_applicants.filter(status='interview_scheduled')
   elif sort == 'in_progress':
      sort_applicants = sort_applicants.filter(status='interview_in_progress')
   elif sort == 'completed':
      sort_applicants = sort_applicants.filter(status='interview_completed')
   else:
      sort_applicants = sort_applicants

   interview_num = applicants.filter(~Q(status='submitted')).count()
   ctx = {"applicants":applicants, "sort_applicants":sort_applicants, "pk":pk, "interview_num": interview_num}
   return render(request, "mainboard.html", ctx)