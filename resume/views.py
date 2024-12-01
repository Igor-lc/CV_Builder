# resume/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume

# Функція створення резюме
def create_resume(request):
    """
    resume/views.py: create_resume
    Створення нового резюме.
    """
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume:resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resume/create_resume.html', {'form': form})

# Функція для відображення списку резюме
def resume_list(request):
    """
    resume/views.py: resume_list
    Відображення списку всіх резюме.
    """
    resumes = Resume.objects.all()
    return render(request, 'resume/resume_list.html', {'resumes': resumes})

# Функція для відображення деталей резюме
def resume_detail(request, pk):
    """
    resume/views.py: resume_detail
    Відображення деталей конкретного резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/resume_detail.html', {'resume': resume})

# Функція для редагування резюме
def edit_resume(request, pk):
    """
    resume/views.py: edit_resume
    Редагування існуючого резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume:resume_detail', pk=resume.pk)
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'resume/edit_resume.html', {'form': form, 'resume': resume})

# Функція для підтвердження видалення резюме
def delete_resume_confirmation(request, pk):
    """
    resume/views.py: delete_resume_confirmation
    Підтвердження видалення резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/delete_resume_confirmation.html', {'resume': resume})

# Функція для видалення резюме
def delete_resume(request, pk):
    """
    resume/views.py: delete_resume
    Фактичне видалення резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == "POST":
        resume.delete()
        return redirect('resume:resume_list')

    return redirect('resume:delete_resume_confirmation', pk=pk)
