from django.contrib.auth.decorators import login_required

from django.urls import path, include
from . import routes

app_name = 'users'

urlpatterns = [
    path('signup', routes.signup),
    path('login', routes.login),
    path('logout', routes.logout),
    # path('update', ),
    # path('register/candidate')
]
