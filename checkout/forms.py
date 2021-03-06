"""
Boardgame Bazaar: checkout App - Forms
"""


from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Displayed within the checkout page; form for customer to fill in contact
    and delivery details for order.  Or is pre-filled from saved information
    in customer account
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'country',)

    def __init__(self, *args, **kwargs):
        """
        Overides init method Add placeholders and classes, remove
        auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # dictionary of placeholders that will show in the form fields.
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
        }

        # ensures cursor starts in full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # interates through fields to apply the below:
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # adds a star to required fields
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Sets the placeholder content to value defined in dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # removes form labels
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
