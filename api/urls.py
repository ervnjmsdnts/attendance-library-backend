from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/attendance/', include('attendance.urls')),
    path('api/library/', include('library.urls')),
]
