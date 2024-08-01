from django.urls import path
from . import views

app_name = 'template'

urlpatterns = [
    path('apply/create',views.ApplicationTemplateCreateView.as_view(), name='apply_create'),

]