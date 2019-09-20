from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from hierarchdata.admin import FileAdmin
from hierarchdata.models import File
from hierarchdata.views import home

admin.site.register(File, FileAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # url('', HomeView.as_view(), name="home"), #tweet/
    
]
