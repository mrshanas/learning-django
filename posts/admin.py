from django.contrib import admin
from .models import Image
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Managing images"""

    list_display = ('title','url','slug','user','created',)

    list_filter = ('created',)