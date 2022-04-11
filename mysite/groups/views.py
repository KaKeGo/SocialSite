from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Group
# Create your views here.


class GroupsView(generic.ListView):
    template_name = 'groups/groups.html'
    model = Group
    context_object_name = 'groups'

def groups_data_view(request):
    groups = Group.objects.all()

    data = []
    for g in groups:
        items = {
            'id': g.id,
            'name': g.name,
            'description': g.description,
            'total_members': g.total_members,
            'gavatar': g.gavatar.url,
        }
        data.append(items)
    return JsonResponse({'data':data})
