# resume/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm, WorkExperienceFormSet  # Додано імпорт форми для досвіду роботи
from .models import Resume

# Функція створення резюме
def create_resume(request):
    """
    resume/views.py: create_resume
    Створення нового резюме з можливістю додавання досвіду роботи.
    """
    if request.method == "POST":
        form = ResumeForm(request.POST)
        work_experience_formset = WorkExperienceFormSet(request.POST)  # Отримання даних з форми досвіду роботи

        # Перевірка, чи є валідними форми для резюме та досвіду роботи
        if form.is_valid() and work_experience_formset.is_valid():
            resume = form.save()  # Збереження резюме

            # Збереження досвіду роботи
            for work_experience_form in work_experience_formset:
                work_experience = work_experience_form.save(commit=False)
                work_experience.resume = resume  # Прив'язуємо досвід роботи до цього резюме
                work_experience.save()

            return redirect('resume:resume_list')  # Перехід до списку резюме
    else:
        form = ResumeForm()
        work_experience_formset = WorkExperienceFormSet()  # Створення порожніх форм для досвіду роботи

    return render(
        request,
        'resume/create_resume.html',
        {'form': form, 'work_experience_formset': work_experience_formset}
    )

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
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=resume)
        work_experience_formset = WorkExperienceFormSet(request.POST, instance=resume)

        if form.is_valid() and work_experience_formset.is_valid():
            # Перевірка на видалення досвіду роботи
            for form in work_experience_formset:
                if form.cleaned_data.get('DELETE'):
                    work_experience = form.save(commit=False)
                    work_experience.delete()

            form.save()  # Зберігаємо зміни в резюме
            work_experience_formset.save()  # Зберігаємо зміни в досвіді роботи

            return redirect('resume:resume_detail', pk=resume.pk)

    else:
        form = ResumeForm(instance=resume)
        work_experience_formset = WorkExperienceFormSet(instance=resume)

    return render(
        request,
        'resume/edit_resume.html',
        {'form': form, 'work_experience_formset': work_experience_formset, 'resume': resume}
    )


# Функція для підтвердження видалення резюме
def delete_resume_confirmation(request, pk):
    """
    resume/views.py: delete_resume_confirmation
    Підтвердження видалення резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == 'POST':
        # Перевірка, чи галочка підтвердження була поставлена
        if 'delete_confirm' in request.POST:
            resume.delete()
            return redirect('resume:resume_list')

    return render(request, 'resume/delete_resume_confirmation.html', {'resume': resume})


# Функція для видалення резюме
def delete_resume(request, pk):
    """
    resume/views.py: delete_resume
    Фактичне видалення резюме.
    """
    resume = get_object_or_404(Resume, pk=pk)

    if request.method == "POST":
        resume.delete()  # Видалення резюме
        return redirect('resume:resume_list')  # Перехід до списку резюме

    return redirect('resume:delete_resume_confirmation', pk=pk)
