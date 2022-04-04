from django.contrib import admin

from .models import User, Profile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login')
    list_filter = ('email', 'username', 'is_staff', 'is_admin')
    ordering = ('-date_joined',)
    list_display = ('email', 'username')
    fieldsets = (
        ('Info', {'fields': ('email', 'username', 'password')}),
        ('permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff', 'is_active', 'regiment')})
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user', 'first_name', 'last_name')
    ordering = ('first_name',)
    list_display = ('user', 'first_name', 'last_name')
    fieldsets = (
        ('info', {'fields': ('user', 'avatar')}),
        ('Personal', {'fields': ('first_name', 'last_name', 'bio')}),
        ('Additional', {'fields': ('slug',)})
    )
