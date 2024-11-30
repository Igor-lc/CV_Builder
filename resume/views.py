from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm
from .models import Resume


def create_resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume:resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resume/create_resume.html', {'form': form})


def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume/resume_list.html', {'resumes': resumes})


def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume/resume_detail.html', {'resume': resume})