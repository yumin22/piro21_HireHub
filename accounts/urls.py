from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("mainboard/<int:pk>/", views.mainboard, name="mainboard"),
]