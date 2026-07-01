from django.contrib import admin
from django.urls import path, include
from course.views import hello_api

urlpatterns = [
    path('', hello_api),
    path('admin/', admin.site.urls),
    path('api/', include('course.urls')),
]