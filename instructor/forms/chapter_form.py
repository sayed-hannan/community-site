from django import forms
from course.models import Chapter



class ChapterCreationForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['course', 'title']