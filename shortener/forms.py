from django import forms

from .models import ShortenedUrl

class ShortenUrlForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ('url', )