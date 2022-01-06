from django.urls import path
from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('create/',views.image_create,name='image_create'),
]