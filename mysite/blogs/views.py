from django.shortcuts import render, resolve_url
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Posts
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'blogs/home.html'
    model = Posts
    context_object_name = 'posts'

@login_required()
def home_post_data_view(request):
    posts = Posts.objects.all()

    data = []
    for post in posts:
        item = {
            'id': post.id,
            'author': post.author.username,
            'body': post.body,
            'image': post.image.url,
            'create_on': post.create_on,
        }
        data.append(item)
    return JsonResponse({'data': data})
