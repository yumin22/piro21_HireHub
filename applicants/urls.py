from django.urls import path
from . import views

app_name = 'applicants'

urlpatterns = [
    path("interview", views.interview, name="interview"),
    path("document", views.document, name="document"),
    path('search_applicant/', views.search_applicant, name='search_applicant'),
    path("document/profile/<int:pk>", views.profile, name='profile'),
    path('apply/<int:pk>/', views.apply, name='apply'),
    path("schedule", views.schedule, name='schedule'),
    path("auto_schedule", views.auto_schedule, name='auto_schedule'),
    path("document/profile/<int:pk>/comment/", views.comment, name='comment'),
    path("applycheck/", views.apply_check, name='apply_check'),
    path("applyresult/", views.apply_result, name='apply_result'),
]