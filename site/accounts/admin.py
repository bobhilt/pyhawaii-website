from django.contrib import admin

from djangae.contrib.gauth_datastore.models import Group as GaeGroup
from django.contrib.auth.models import Group

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_service', 'is_superuser')
    list_filter = ('is_active', 'is_superuser', 'is_staff', 'is_service')

    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (
            None, {
                'fields': ('username', 'date_joined', 'last_login')
            }
        ),
        (
            'Account Type', {
                'fields': ('is_active', 'is_staff', 'is_service', 'is_superuser')
            }
        ),
        (
            'Contact', {
                'fields': ('email', 'first_name', 'last_name')
            }
        ),
        (
            'Permissions', {
                'fields': ('user_permissions',)
            }
        ),
    )


admin.site.unregister(Group)
admin.site.unregister(GaeGroup)
