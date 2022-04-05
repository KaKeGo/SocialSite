from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth.decorators import login_required

from .models import Posts
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'blogs/home.html'
    model = Posts
    context_object_name = 'posts'
