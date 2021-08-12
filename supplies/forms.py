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

        self.fields['category'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input'
