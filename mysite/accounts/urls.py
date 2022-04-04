from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    FirstView,
)


app_name = 'accounts'

urlpatterns = [
    path('', FirstView, name='first'),
]