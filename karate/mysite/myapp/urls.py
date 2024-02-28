from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.hello,name='hello'),
    path('signup/',views.signup,name="signup"),
    path('gym/',views.gym,name="gym"),
    path('member/',views.member,name="member"),
    path('lider/',views.lider,name='lider'),
    path('index/',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='myapp/change_password.html'),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='myapp/change_password_done.html'),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='myapp/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_view.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'),name='password_reset_complete')

   
]