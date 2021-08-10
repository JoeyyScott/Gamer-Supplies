from django import forms
from .models import Order


# Form for orders
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'contact_number',
            'address_line_1', 'address_line_2',
            'town_or_city', 'county',
            'postcode', 'country')

    def __init__(self, *args, **kwargs):
        # Set autofocus on first name field and add placeholders
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'contact_number': 'Contact Number (optional)',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'town_or_city': 'Town/City',
            'county': 'County (optional)',
            'postcode': 'Postcode (optional)',
        }

        # Setting form up for the user
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                # Append * to required fields
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Append placeholders using above data
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            # Remove default labels
            self.fields[field].label = False
