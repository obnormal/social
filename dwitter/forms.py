from django import forms

from dwitter.models import Dweet


class DweetForm(forms.ModelForm):
    text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-info is-medium",
            }
        ),
        label="",)

    class Meta:
        model = Dweet
        exclude = ("user", )