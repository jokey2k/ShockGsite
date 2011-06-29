from django import forms
import settings

from django.core import validators

class ShoutboxPostForm(forms.Form):
    nickname = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    hint = forms.RegexField(settings.SIMPLE_REGEX, max_length=100)
    next = forms.CharField(widget=forms.HiddenInput, required=False)
