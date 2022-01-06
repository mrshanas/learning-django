from django.urls import path,reverse_lazy
from django.urls.conf import include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # THIS was the normal authentication
    # path('login/',views.user_login,name='user_login'),

    # from django
    path('',views.dashboard,name='dashboard'),
    # register url
    path('register',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    # password resets urls
    path('password_reset/',auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')),name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # if you dont want to hard code authentication
    # path('',include('django.contrib.auth.urls')),
    # path('dashboard',views.dashboard,name='dashboard')

    # edit user profiles
    path('edit/',views.edit,name='edit'),
]