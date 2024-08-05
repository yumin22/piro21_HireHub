from django.contrib import admin
from .models import Application, ApplicationTemplate, Question, Answer, Possible_date_list

# Register your models here.

admin.site.register(Application)
admin.site.register(ApplicationTemplate)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Possible_date_list)