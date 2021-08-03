from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# Modified django github class
# source: https://github.com/django/django/blob/main/django/forms/widgets.py
class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove image')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'supplies/custom_widget_templates/custom_clearable_file_input.html'
