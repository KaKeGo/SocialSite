from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import User
from .forms import UserCreateForm
# Create your views here.


def FirstView(request):
    return render(request, 'accounts/home.html')

class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:first')
