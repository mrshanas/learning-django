from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
    """Allow users to upload images"""
    class Meta:
        model = Image

        fields = ['title','url','description']

        widgets = {
            'url':forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg','jpeg']

        extension = url.rsplit('.')[1].lower()

        if extension not in valid_extensions:
            raise forms.ValidationError('The image provided is not jpg or jpeg format')

        return url