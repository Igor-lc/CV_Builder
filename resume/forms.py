# resume/forms.py
# Форми для роботи з моделями Resume та WorkExperience.

from django import forms
from django.forms import inlineformset_factory
from .models import Resume, WorkExperience


class ResumeForm(forms.ModelForm):
    """
    Форма для створення та редагування основних даних резюме.
    """
    class Meta:
        model = Resume
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address',
            'about_me', 'skills', 'education',
            'institution_name', 'education_degree', 'graduation_date'
        ]


# Форма для роботи з досвідом роботи (inline formset)
WorkExperienceFormSet = inlineformset_factory(
    Resume,  # Модель, до якої прив'язано formset
    WorkExperience,  # Модель досвіду роботи
    fields=['job_title', 'company_name', 'job_description', 'start_date', 'end_date'],
    extra=1,  # Кількість додаткових порожніх форм
    can_delete=True  # Можливість видалення записів
)
