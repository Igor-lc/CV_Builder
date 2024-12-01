# resume/urls.py

from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    # Сторінка створення нового резюме
    path('create/', views.create_resume, name='create_resume'),

    # Головна сторінка зі списком резюме
    path('', views.resume_list, name='resume_list'),

    # Детальна сторінка резюме
    path('<int:pk>/', views.resume_detail, name='resume_detail'),

    # Сторінка редагування резюме
    path('<int:pk>/edit/', views.edit_resume, name='edit_resume'),

    # Сторінка підтвердження видалення резюме
    path('<int:pk>/delete/', views.delete_resume_confirmation, name='delete_resume_confirmation'),

    # Сторінка видалення резюме
    path('<int:pk>/delete/confirm/', views.delete_resume, name='delete_resume'),
]
