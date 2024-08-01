from django.urls import path
from . import views

app_name = 'template'

urlpatterns = [
    path('list/', views.TemplateListView.as_view(), name ='template_list'),
    path('apply/create',views.ApplicationTemplateCreateView.as_view(), name='apply_create'),
    path('apply/<int:pk>', views.TemplateDetailView.as_view(), name='template_detail'),
]