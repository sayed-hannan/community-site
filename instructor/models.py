from django.db import models
from django.contrib.auth.models import User  # If you want to link instructors to user accounts
from course.models import Course  # Import the Course model from your existing app

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    # Add any additional fields for instructors, e.g., profile picture, bio, etc.

class InstructorCourse(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
