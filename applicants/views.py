from django.shortcuts import render, redirect
from .forms import ApplicationForm, QuestionFormSet
from .models import ApplicationTemplate



def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        formset = QuestionFormSet(request.POST, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('/')  # 적절한 URL로 리다이렉트
    else:
        form = ApplicationForm()
        formset = QuestionFormSet(instance=form.instance)
    
    return render(request, 'applicant_temp.html', {'form': form, 'formset': formset})
    