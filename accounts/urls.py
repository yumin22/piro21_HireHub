from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
   path('', initialInterviewer, name='initialInterviewer'),
   path('initialApplicant/', initialApplicant, name='initialApplicant'),
   path('signup/', signup, name='signup'),
   path('signup/check/', signupCheck, name='signupCheck'),
   path('login/', login, name='login'),
   path('login/require_approval', requiredApproval, name='requiredApproval'),
   path('logout/', logout, name='logout'),  
   path("mainboard/<int:pk>/", mainboard, name="mainboard"),
]