from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    # The meta class allows us to
    # provide custom behavior and settings
    # to the generic ModelForm class
    # without altering or overriding its code
    # this is an example of meta programming
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }