from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Course  

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'blog.html', {'posts': posts})

def single_blog(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'single-blog.html', {'post': post})

def course(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'course.html', {'courses': courses})

def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)  
    return render(request, 'course-details.html', {'course': course})


def join_course(request):
    return render(request, 'join_course.html')  

def our_campus(request):
    return render(request, 'our_campus.html')  #