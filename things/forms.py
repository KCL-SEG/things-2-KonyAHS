from django import forms
from .models import Thing
"""Forms of the project."""

# Create your forms here.


class ThingForm(forms.ModelForm):
    """Form for the Thing model."""
    name = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '35'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': '120'}))
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {

            'quantity': forms.NumberInput
        }