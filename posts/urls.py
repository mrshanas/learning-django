from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create',views.post_create,name='create'),
    path('detail/<int:id>/<slug:slug>',views.post_detail,name='post_detail'),
    path('like',views.post_like,name='like'),
    path('',views.post_list,name='post_list')
]