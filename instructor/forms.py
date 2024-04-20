# instructor/forms.py
from django import forms
from course.models import Course, Chapter, Topic

class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class ChapterCreationForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['course', 'title']

class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['chapter', 'title', 'content']
