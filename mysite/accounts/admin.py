from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Profile
from .forms import UserCreateForm, UserChangeForm
# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    filter_horizontal = ()
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
        ('Personal', {'fields': ('first_name', 'last_name', 'bio', 'motto')}),
        ('Additional', {'fields': ('slug',)})
    )

admin.site.register(User, UserAdmin)
