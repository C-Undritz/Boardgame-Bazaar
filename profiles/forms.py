"""
Boardgame Bazaar: profiles App - Forms
"""


from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserAddressForm(forms.ModelForm):
    """
    Form that allows the customer to enter, or displays, contact and address
    details
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'wishlist')

    def __init__(self, *args, **kwargs):
        """
        Overides init method Add placeholders and classes, remove
        auto-generated labels and sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # dictionary of placeholders that will show in the form fields.
        placeholders = {
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
            'default_phone_number': 'Phone Number',
        }

        # Interates through fields to apply the below:
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    # Adds a star to required fields
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Sets the placeholder content to value defined in dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Removes form labels
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'profile-form-input'


class UserForm(forms.ModelForm):
    """
    Form that allows the customer to enter, or displays, user account details.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
