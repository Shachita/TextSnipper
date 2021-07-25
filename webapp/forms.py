from django import forms
from django.forms import ModelForm

from .models import TextSnippet

class SnippetForm(ModelForm):
    shareable_text = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows": 15, "cols": 120})
    )
    secret_key = forms.CharField(required=False)


    class Meta:
        model = TextSnippet
        fields = ("shareable_text", "secret_key", )

