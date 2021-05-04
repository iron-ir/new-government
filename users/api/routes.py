import logging
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as dj_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound
from django.views.decorators.http import require_POST, require_GET
from django.contrib import messages
import re

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from users.models import User
from repository.response import true_response, false_response
from .serializers import UserLoginSerializer


@require_POST
def login(request: HttpRequest):
    if not request.user.is_anonymous:
        usr = request.user
        return false_response(
            message='شما در حال حاظر ورود کرده اید.',
        )
    if 'username' not in request.POST:
        return false_response(
            message='فیلد مربوط به نام کاربری- نام کاربری یا شماره تلفن ویا ایمیل- خالی است.',
        )
    if 'password' not in request.POST:
        return false_response(
            message='فبلد مربوط به کلمه عبور خالی می باشد.',
        )
    usr = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if usr is None:
        return false_response(
            message='کاربری با این مشخصات وجود ندارد.',
        )
    dj_login(request, usr)
    return true_response(
        message='ورود کاربر با موفقیت صورت گرفت.',
        data={
            'user': usr.to_dict(),
        }
    )


@require_GET
def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return true_response(
        message='خروج با موفقیت صورت گرفت.',
    )
