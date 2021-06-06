from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('app/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]