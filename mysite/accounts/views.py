from django.shortcuts import render, redirect
from django.views import generic

# Create your views here.


def FirstView(request):
    return render(request, 'accounts/home.html')
