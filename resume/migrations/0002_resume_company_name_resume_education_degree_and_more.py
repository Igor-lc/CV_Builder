# Generated by Django 5.1.3 on 2024-11-28 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='education_degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='graduation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='institution_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='job_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
