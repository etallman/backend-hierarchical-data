from django.contrib import admin
from django.urls import path

from hierarchdata.admin import FileAdmin
from hierarchdata.models import File

admin.site.register(File, FileAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
]
