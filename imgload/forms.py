from django import forms
from .models import Image_model
from django.core.exceptions import ValidationError


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image_model
        fields = ['img', 'url']

    def clean(self):
        cleaned_data = super().clean()
        img = cleaned_data.get('img')
        url = cleaned_data.get('url')

        if not (img or url):
            raise ValidationError("Provide at least one of fields!")
        if img and url:
            raise ValidationError("Please submit only one field!")


class ResizeForm(forms.Form):
    height = forms.IntegerField(label='height')
    width = forms.IntegerField(label='width')
