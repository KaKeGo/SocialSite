from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import resolve_url
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import User, Profile
from .forms import UserCreateForm
# Create your views here.


def FirstView(request):
    return render(request, 'accounts/home.html')

class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:first')

class SigninView(LoginView):
    template_name = 'accounts/signin.html'

    def get_success_url(self):
        return resolve_url('accounts:first')

@login_required()
def logout_view(request):
    logout(request)
    return redirect('accounts:first')

class ProfileView(generic.DetailView):
    template_name = 'accounts/profile.html'
    model = Profile
    context_object_name = 'profile'
    slug_url_kwarg = 'slug'
