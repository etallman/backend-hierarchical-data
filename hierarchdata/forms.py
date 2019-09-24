from django import forms
from .models import File

class FileForm(forms.Form):
    name = forms.CharField(max_length=40)
    description=forms.CharField(max_length=100)
    folder = forms.ModelChoiceField(queryset=File.objects.all())
    
