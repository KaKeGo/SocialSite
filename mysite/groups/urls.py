from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
 GroupsView,
)


app_name = 'groups'

urlpatterns = [
    path('groups/', login_required(GroupsView.as_view()), name='groups'),
]
