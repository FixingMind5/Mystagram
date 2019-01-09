"""User admin classes"""

from django.contrib import admin
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
