from django.shortcuts import render, resolve_url, get_object_or_404
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
def home_post_data_view(request, num_posts):
    visible = 1
    upper = num_posts
    lower = upper - visible
    size = Posts.objects.all().count()

    posts = Posts.objects.all()

    data = []
    for post in posts:
        item = {
            'id': post.id,
            'author': post.author.user.username,
            'avatar': post.author.avatar.url,
            'body': post.body,
            'total_likes': post.total_likes,
            'image': post.image.url,
            'create_on': post.create_on,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size':size})
