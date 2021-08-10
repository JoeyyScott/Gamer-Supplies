from django import forms
from .models import UserProfile


# User profile form
class FormUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Set autofocus on first field and add placeholders
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email',
            'default_contact_number': 'Contact Number',
            'default_address_line_1': 'Address Line 1',
            'default_address_line_2': 'Address Line 2',
            'default_town_or_city': 'Town/City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                # Append * to required fields
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                # Append placeholders using above data
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            # Remove default labels
            self.fields[field].label = False
