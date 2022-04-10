from django.shortcuts import render
from django.views import generic

from .models import Group
# Create your views here.


class GroupsView(generic.ListView):
    template_name = 'groups/groups.html'
    model = Group
    context_object_name = 'groups'
