# resume/models.py
# Моделі для зберігання даних резюме та досвіду роботи.

from django.db import models


class Resume(models.Model):
    """
    Модель для зберігання основних даних про резюме.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    institution_name = models.CharField(max_length=100, null=True, blank=True)
    education_degree = models.CharField(max_length=100, null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WorkExperience(models.Model):
    """
    Модель для зберігання досвіду роботи, пов'язаного з резюме.
    """
    resume = models.ForeignKey(Resume, related_name="work_experiences", on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Якщо це поточна робота, поле може бути порожнім

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
