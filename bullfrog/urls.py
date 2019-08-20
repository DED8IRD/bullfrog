from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('vue.urls')),
    path('djangogirls', include('blog.urls')),
    path('admin/', admin.site.urls),
]