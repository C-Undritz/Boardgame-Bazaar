"""
Boardgame Bazaar: mailing_list App - Admin
"""


from django.contrib import admin
from .models import MailingList


class MailingListAdmin(admin.ModelAdmin):
    """
    Display for MailingList model fields in admin
    """
    list_display = (
        'email',
        'date_added',
    )

    ordering = ('date_added',)


admin.site.register(MailingList, MailingListAdmin)
