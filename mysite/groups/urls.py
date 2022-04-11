from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
GroupsView,
groups_data_view,
)


app_name = 'groups'

urlpatterns = [
    path('', login_required(GroupsView.as_view()), name='groups'),
    path('data/', groups_data_view, name='groups_data'),
]
