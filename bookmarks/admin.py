from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdminManager(admin.ModelAdmin):
    """Manage the image model in admin panel"""

    list_display = ['title','slug','url','user','image']

    list_filter = ['created']