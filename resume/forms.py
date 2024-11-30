from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address',
            'about_me', 'skills', 'work_experience', 'education',
            'institution_name', 'company_name', 'job_description',
            'job_title', 'start_date', 'end_date', 'education_degree',
            'graduation_date'
        ]
