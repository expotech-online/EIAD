from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)  # E.g., "3 weeks"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(default="No excerpt available")  # Optional default
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Allow nulls
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
