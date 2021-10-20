"""
Boardgame Bazaar: profiles App - Admin
"""


from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Sets out the database fields from the User model visible in admin.
    """
    list_display = (
        'user',
    )


admin.site.register(UserProfile, UserProfileAdmin)
