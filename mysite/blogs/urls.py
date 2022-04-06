from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    HomeView,
    home_post_data_view,
)


app_name = 'blogs'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('data/', home_post_data_view, name='home-data'),
]
