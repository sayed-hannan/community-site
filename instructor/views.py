# instructor/views.py
from django.shortcuts import render, redirect
from .forms import CourseCreationForm, ChapterCreationForm, TopicCreationForm
from course.models import Course, Chapter, Topic

def dashboard(request):
    return render(request, 'dashboard.html;')


def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_chapter')  # Redirect to instructor dashboard or any other page
    else:
        form = CourseCreationForm()
    
    return render(request, 'create_course.html', {'form': form})

def create_chapter(request):
    if request.method == 'POST':
        form = ChapterCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_topic')  # Redirect to instructor dashboard or any other page
    else:
        form = ChapterCreationForm()
    
    return render(request, 'create_chapter.html', {'form': form})

def create_topic(request):
    if request.method == 'POST':
        form = TopicCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to instructor dashboard or any other page
    else:
        form = TopicCreationForm()
    
    return render(request, 'create_topic.html', {'form': form})
