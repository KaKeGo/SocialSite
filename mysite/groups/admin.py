from django.contrib import admin

from .models import Group, GroupPost, Regiment

# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_members', 'create_on')
    list_filter = ('name', 'create_on')

@admin.register(GroupPost)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('body', 'author')
    list_filter = ('body', 'author')

@admin.register(Regiment)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
