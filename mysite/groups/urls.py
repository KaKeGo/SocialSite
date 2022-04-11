from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
GroupsView,
groups_data_view,
GroupsDetailView,
GroupInfoDetailView,
GroupMembersDetailView,
GroupGalleryDetailView,
GroupCreateView,
)


app_name = 'groups'

urlpatterns = [
    path('', login_required(GroupsView.as_view()), name='groups'),
    path('create/', login_required(GroupCreateView.as_view()), name='create'),
    path('data/', groups_data_view, name='groups_data'),
    path('<slug:slug>/', login_required(GroupsDetailView.as_view()), name='detail'),
    path('<slug:slug>/info/', login_required(GroupInfoDetailView.as_view()), name='detail_info'),
    path('<slug:slug>/members/', login_required(GroupMembersDetailView.as_view()), name='detail_members'),
    path('<slug:slug>/gallery/', login_required(GroupGalleryDetailView.as_view()), name='detail_gallery'),
]
