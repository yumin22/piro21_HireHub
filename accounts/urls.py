from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("<int:pk>/mainboard", views.mainboard, name="mainboard"),
]