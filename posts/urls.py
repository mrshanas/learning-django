from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create',views.create_image,name='create')
]