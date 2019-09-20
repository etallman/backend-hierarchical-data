from django.views import View
from .models import File
from hierarchdata import urls
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse

# class HomeView(View):
#     # model = File
#     template_name = 'home.html'

def home(request, *args, **kwargs):
    html = 'home.html'
    items = File.objects.all()
    return render(request, html, {'file': items})
    