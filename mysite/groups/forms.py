from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = ('name', 'founder', 'gavatar', 'description', )
