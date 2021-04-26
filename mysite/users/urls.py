from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.singup_form, name='signup_form'),
    path('signup/done', views.singup_done, name='signup_done'),

    path('vcode', views.vcode_form, name='vcode_form'),
    path('vcode/done', views.vcode_done, name='vcode_done'),

    path('login', views.login_form, name='login_form'),
    path('login/done', views.login_done, name='login_done'),

    path('logout', views.logout_form, name='logout_form'),
    path('logout/done', views.logout_done, name='logout_done'),

    path('password/reset', views.password_reset_form, name='password_reset_form'),
    path('password/reset/done', views.password_reset_done, name='password_reset_done'),
]
