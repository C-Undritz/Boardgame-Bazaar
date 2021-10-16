from django import forms
from .models import MailingList


class DateInput(forms.DateInput):
    input_type = 'date'


class AddToMailingList(forms.ModelForm):

    class Meta:
        model = MailingList
        fields = ('email',)
