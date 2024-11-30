from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('create/', views.create_resume, name='create_resume'),
    path('', views.resume_list, name='resume_list'),
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
]
