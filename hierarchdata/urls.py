from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from hierarchdata.admin import FileAdmin
from hierarchdata.models import File
from hierarchdata.views import show_files, add_file

admin.site.register(File, FileAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_files, name='filetree'),
    path('addfile/', add_file),
]
