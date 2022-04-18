from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Тақырып",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=2, label="URL")
    is_published = forms.BooleanField(label="Шығарылым", required=False, initial=True)


