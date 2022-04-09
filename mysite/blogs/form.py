from django import forms

from .models import Blogs


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('body', 'image', 'author')
