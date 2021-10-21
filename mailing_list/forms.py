"""
Boardgame Bazaar: mailing_list App - Forms
"""


from django import forms
from .models import MailingList


class DateInput(forms.DateInput):
    input_type = 'date'


class AddToMailingList(forms.ModelForm):
    """
    Form for users to add email to mailing list database
    """
    class Meta:
        model = MailingList
        fields = ('email',)
