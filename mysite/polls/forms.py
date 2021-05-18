from django import forms
from .models import Choice
from django.utils.translation import gettext_lazy as _

class ChoiceForm(forms.Form):
    class Meta:
        model = Choice
        fields = ['choice_text']
        labels = {
            'choice_text': _('What is the choice of question'),
        }
        help_texts = {
            'choice_text': _('Some useful help text.'),
        }
        error_messages = {
            'choice_text': {
                'choice_text': _("This choice has already exist."),
            },
        }