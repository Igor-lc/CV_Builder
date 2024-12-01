# resume/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Resume, WorkExperience


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address',
            'about_me', 'skills', 'education',
            'institution_name', 'education_degree', 'graduation_date'
        ]


# Динамічна форма для досвідів роботи
WorkExperienceFormSet = inlineformset_factory(
    Resume,  # Пов'язана модель
    WorkExperience,  # Модель досвіду роботи
    fields=['job_title', 'company_name', 'job_description', 'start_date', 'end_date'],
    extra=1,  # Додаткова порожня форма
    can_delete=True  # Можливість видаляти записи
)
