from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Course  
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_data = form.save()
            
            subject = f"New Contact Form Submission from {contact_data.name}"
            message = f"Name: {contact_data.name}\nEmail: {contact_data.email}\nPhone: {contact_data.phone}\nCompany: {contact_data.company}\nMessage: {contact_data.message}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            user_message = f"Hello {contact_data.name},\n\nThank you for contacting us! We have received your message and will get back to you soon.\n\nBest regards,\nYour Company Name"
            send_mail(
                "Thank you for your message!",
                user_message,
                settings.EMAIL_HOST_USER,
                [contact_data.email],
                fail_silently=False,
            )
            
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

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