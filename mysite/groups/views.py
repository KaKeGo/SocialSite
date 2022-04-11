from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy

from .models import Group
from .forms import GroupCreateForm
# Create your views here.


class GroupCreateView(generic.CreateView):
    template_name = 'groups/group_create.html'
    model = Group
    form_class = GroupCreateForm
    context_object_name = 'group'
    success_url = reverse_lazy('groups:groups')

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

class GroupsDetailView(generic.DetailView):
    template_name = 'groups/group_detail.html'
    model = Group
    context_object_name = 'group'
    slug_field = 'slug'

class GroupInfoDetailView(generic.DetailView):
    template_name = 'groups/group_info.html'
    model = Group
    context_object_name = 'group'
    slug_field = 'slug'

class GroupMembersDetailView(generic.DetailView):
    template_name = 'groups/group_members.html'
    model = Group
    context_object_name = 'group'
    slug_field = 'slug'

class GroupGalleryDetailView(generic.DetailView):
    template_name = 'groups/group_gallery.html'
    model = Group
    context_object_name = 'group'
    slug_field = 'slug'
