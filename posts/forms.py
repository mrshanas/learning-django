from django import forms
from .models import Post
from django.utils.text import slugify


class PostCreateForm(forms.ModelForm):
    """A form to manage the posts by users"""

    class Meta:
        model = Post

        fields = ['title','image','caption',]
        
    # def save(self,force_insert=False,force_update=False,commit=True):
    #     post = super().save(commit=False)
    #     post_name = self.cleaned_data['image']
    #     title = slugify(post.title)
    #     ext = post_name.rsplit('.',1)[1].lower()
    #     name = f"{title}.{ext}"
    #     post.image = name

    #     if commit:
    #         post.save()
    #     return post

        


