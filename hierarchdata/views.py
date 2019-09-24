from django.views import View
from .models import File
from hierarchdata import urls
from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import FileForm


def show_files(request, *args, **kwargs):
    html = 'filetree.html'
    items = File.objects.all()
    return render(request, html, {'file': items})

# Extra credit portion -- add folder and file
def add_file(request, *args, **kwargs):
    html = 'form.html'
   
    if request.method == "POST":
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'], 
                description=data['description'], 
                parent=data['folder']
            )
            return  HttpResponseRedirect(reverse('filetree'))
   
    form = FileForm()
    
    return render(request, html, {'form': form})   
    