from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal', {
            'fields': ('first_name', 'last_name')
        }),
        ('Role', {'fields': ('is_superuser',)}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
