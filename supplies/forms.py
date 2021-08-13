# Imports
from django import forms
from .widgets import CustomClearableFileInput
from .models import Supply, Category


# Supply form
class FormSupply(forms.ModelForm):

    class Meta:
        model = Supply
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'\
            placeholder': 'Supply Name', 'class': 'altFont'}),
            'price': forms.TextInput(attrs={'\
            placeholder': 'Amount (GBP)', 'class': 'altFont'}),
            'description': forms.TextInput(attrs={'\
            placeholder': 'Supply description', 'class': 'altFont'}),
            'brand': forms.TextInput(attrs={'\
            placeholder': 'Supply brand', 'class': 'altFont'}),
            'size': forms.TextInput(attrs={'\
            placeholder': 'Supply size', 'class': 'altFont'}),
        }

    # Credit for overriding image field with custom input
    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.get_name()) for c in categories]

        # Setting up form for the superuser
        self.fields['category'].choices = names
        self.fields['name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            if field == 'price':
                self.fields[field].widget.attrs['min'] = 0.0099
            field.widget.attrs['class'] = 'form-input'

    # Credit for adapted check amount value - see README.md for more details
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0.0099:
            raise forms.ValidationError("Amount cannot be less than 0.01")
        return price
