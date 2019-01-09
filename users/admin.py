"""User admin classes"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Class profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('website', 'picture', 'phone_number')
    search_fields = (
                  'user__username',
                  'user__email',
                  'user__first_name',
                  'user__last_name',
                  'phone_number'
              )

    list_filter = (
                'created',
                'modified',
                'user__is_active',
                'user__is_staff'
            )


    fieldsets = (
        ('Profile', {
            'fields': (
                 ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('modified'),),
        })
    )

    readonly_fields = ('created', 'modified')


class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)