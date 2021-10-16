from django.contrib import admin
from .models import MailingList


class MailingListAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_added',
    )

    ordering = ('date_added',)


admin.site.register(MailingList, MailingListAdmin)
