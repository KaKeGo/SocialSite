from django.contrib import admin

from .models import Posts
# Register your models here.


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'total_likes', 'create_on')
    list_filter = ('author', 'create_on')
