
from django import forms
from .models import TravelBlog
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
    class Meta:
        model = TravelBlog
        fields = ('title', 'author', 'date', 'thumbnail', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'thumbnail': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'})

        }
