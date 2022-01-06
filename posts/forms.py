from django import forms
from .models import Image
from django.utils.text import slugify
from urllib import request
from django.core.files.base import ContentFile

class ImageCreateForm(forms.ModelForm):
    """A form to manage images"""

    class Meta:
        model = Image
        fields = ('title','description','url')

        # the url input wont be visible to users
        widgets = {
            'url':forms.HiddenInput
        }

    def clean_url(self):
        # allow jpeg/jpg uploads only

        extensions = ['jpg','jpeg']
        url = self.cleaned_data['url']
        ext = url.rsplit('.',1)[1].lower()

        if ext not in extensions:
            raise forms.ValidationError('Please use jpg or jpeg types of images')

        return url

    def save(self,force_insert=False,force_update=False,commit=True):
        # override the save method in form class
        image = super().save(commit=False)
        url = self.cleaned_data['url']
        image_name = slugify(image.title)
        extension = url.rsplit('.',1)[1].lower()
        image_url = f"{image_name}.{extension}"

        # download image from url
        response = request.urlopen(url=url)
        image.image.save(image_name,ContentFile(response.read()),save=False)

        if commit:
            image.save()

        return image