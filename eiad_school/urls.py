from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import custom_404
from django.views.static import serve

handler404 = custom_404


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('courses/', include('courses.urls')),
    path('blogs/', include('blogs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

