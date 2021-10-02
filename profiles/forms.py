from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Fields to be rendered in the form.
        exclude = ('user', 'wishlist')

    def __init__(self, *args, **kwargs):
        """
        Overides init method Add placeholders and classes, remove
        auto-generated labels and set autofocus on first field
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

        # ensures cursor starts in full name field
        # self.fields['default_street_address1'].widget.attrs['autofocus'] = True

        # interate through fields to apply the below:
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    # adds a star to required fields
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Sets the placeholder content to value defined in dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # removes form labels
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'profile-form-input'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # Fields to be rendered in the form.
        fields = ('first_name', 'last_name', 'username', 'email',)
