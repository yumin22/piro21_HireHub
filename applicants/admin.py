from django.contrib import admin
from .models import Application, ApplicationTemplate, ApplicationQuestion, Answer
from template.models import EvaluationTemplate

# Register your models here.

admin.site.register(Application)
admin.site.register(ApplicationTemplate)
admin.site.register(ApplicationQuestion)
admin.site.register(EvaluationTemplate)
admin.site.register(Answer)