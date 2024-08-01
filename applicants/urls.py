from django.urls import path
from . import views

app_name = 'applicants'

urlpatterns = [
    path("interview", views.interview, name="interview"),
    path("document", views.document, name="document"),
    path("document/profile/<int:pk>", views.profile, name='profile'),
]