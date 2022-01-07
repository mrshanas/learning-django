from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    """A form to manage the posts by users"""

    class Meta:
        model = Post

        fields = ['title','image','caption']
        
