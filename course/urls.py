from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/chapter/<int:chapter_id>/', views.course_detail, name='chapter_detail'),
    path('course/<int:course_id>/chapter/<int:chapter_id>/topic/<int:topic_id>/', views.course_detail, name='topic_detail'),
]
