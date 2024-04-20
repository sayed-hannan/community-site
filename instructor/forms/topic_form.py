from django import forms
from course.models import  Topic

class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['chapter', 'title', 'content']
        
   