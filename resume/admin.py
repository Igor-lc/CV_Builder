# resume/admin.py

from django.contrib import admin
from .models import Resume, WorkExperience

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_created')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('date_created',)

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('resume', 'job_title', 'company_name', 'start_date', 'end_date')
    search_fields = ('job_title', 'company_name')
    list_filter = ('start_date', 'end_date')
