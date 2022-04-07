from django.shortcuts import render, resolve_url, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Blogs
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'blogs/home.html'
    model = Blogs
    context_object_name = 'posts'

@login_required()
def home_post_data_view(request, num_posts):
    visible = 4
    upper = num_posts
    lower = upper - visible
    size = Blogs.objects.all().count()

    posts = Blogs.objects.all()

    data = []
    for post in posts:
        item = {
            'id': post.id,
            'author': post.author.username,
            'avatar': post.author.profile.avatar.url,
            'body': post.body,
            'liked': True if request.user in post.liked.all() else False,
            'count': post.total_likes,
            'total_likes': post.total_likes,
            'image': post.image.url,
            'create_on': post.create_on,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size':size})

def like_post(request):
    pk = request.POST.get('pk')
    blog = Blogs.objects.get(pk=pk)
    if request.user in blog.liked.all():
        liked = False
        blog.liked.remove(request.user)
    else:
        liked = True
        blog.liked.add(request.user)
    return JsonResponse({'liked': liked, 'count': blog.total_likes})
