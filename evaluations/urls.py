from django.urls import path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('evaluations/create/<int:pk>/', views.create_evaluation, name='evaluation_create'),
]