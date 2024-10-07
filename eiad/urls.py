from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),           # Home page
    path('about/', views.about, name='about'),     # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('blog/', views.blog, name='blog'),        # Blog page
    path('blog/<int:post_id>/', views.single_blog, name='single_blog'), 
    path('course/', views.course, name='course'),  # Course page
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('join_course/', views.join_course, name='join_course'),
    path('our_campus/', views.our_campus, name='our_campus'),
    path('success/', views.success, name='success'),
]
