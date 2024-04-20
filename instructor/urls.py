# instructor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-chapter/', views.create_chapter, name='create_chapter'),
    path('create-topic/', views.create_topic, name='create_topic'),
]


