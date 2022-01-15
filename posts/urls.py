from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create',views.post_create,name='create'),
    path('detail/<int:id>/<slug:slug>',views.post_detail,name='post_detail'),
    path('like',views.post_like,name='like'),
    path('',views.post_list,name='post_list'),
    path('users',views.user_list,name='user_list'),
    path('user/follow',views.user_follow,name='user_follow'),
    path('users/<username>',views.user_detail,name='user_detail'),
    
]