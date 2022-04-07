from django.contrib import admin

from .models import Blogs
# Register your models here.


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('author', 'total_likes', 'create_on')
    list_filter = ('author', 'create_on')
