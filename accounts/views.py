from django.shortcuts import render, redirect
from .models import Interviewer
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def initial(request):
   return render(request, 'accounts/initial.html')

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
               return redirect('accounts:initial') # 수정 필요
            else:
               form.add_error(None, '관리자의 승인이 필요하거나 계정이 비활성화되었습니다.')
         else:
            form.add_error(None, '이메일 또는 비밀번호가 잘못되었습니다.')
   else:
      form = LoginForm()

   context = {'form': form}
   return render(request, 'accounts/login.html', context)
