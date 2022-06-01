from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *

MAX_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields=['content']

    def clean_content(self):
        data = self.cleaned_data["content"]
        if len(data) > MAX_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return data
    