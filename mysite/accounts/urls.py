from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    FirstView,
    SignupView,
    SigninView,
    logout_view,
    ProfileView,
)


app_name = 'accounts'

urlpatterns = [
    path('', FirstView, name='first'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),
    path('profile/<slug:slug>/', login_required(ProfileView.as_view()), name='profile'),
]
