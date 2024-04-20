from django.shortcuts import render, get_object_or_404
from .models import Course, Chapter, Topic


def courses(request):
    # Query the database to retrieve all courses
    all_courses = Course.objects.all()

    # Pass the courses to the template
    context = {'courses': all_courses}
    
    # Render the template with the context data
    return render(request, 'courses.html', context)





from django.shortcuts import render, get_object_or_404
from .models import Course, Chapter, Topic

def course_detail(request, course_id, chapter_id=None, topic_id=None):
    # Retrieve the course object
    course = get_object_or_404(Course, pk=course_id)

    # Retrieve all chapters for the course
    chapters = Chapter.objects.filter(course=course)

    # Initialize variables for selected chapter and topics
    selected_chapter = None
    topics = None
    selected_topic = None

    # Check if a specific chapter is requested
    if chapter_id:
        selected_chapter = get_object_or_404(Chapter, pk=chapter_id)
        topics = Topic.objects.filter(chapter=selected_chapter)
        
        # Check if a specific topic is requested within the selected chapter
        if topic_id:
            selected_topic = get_object_or_404(Topic, pk=topic_id)
    else:
        # If no specific chapter is requested, default to the first chapter
        selected_chapter = chapters.first()
        if selected_chapter:
            topics = Topic.objects.filter(chapter=selected_chapter)
        
            # If the first chapter has topics, default to the first topic
            if topics:
                selected_topic = topics.first()

    context = {
        'course': course,
        'chapters': chapters,
        'selected_chapter': selected_chapter,
        'topics': topics,
        'selected_topic': selected_topic,
    }

    return render(request, 'course_detail.html', context)




