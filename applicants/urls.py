from django.urls import path
from . import views

app_name = 'applicants'

urlpatterns = [
    path('applitemp/', views.create_application, name='applitemp'),
]