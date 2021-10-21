"""
Boardgame Bazaar: mailing_list App - Models
"""


from django.db import models


class MailingList(models.Model):
    """
    Model to record customer email for a mailing list
    """
    email = models.EmailField(null=False, blank=False)
    date_added = models.DateField(auto_now_add=True)
