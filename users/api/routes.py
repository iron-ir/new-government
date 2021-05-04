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
from repository.messages import *
from repository.regular_expression import username_reg, email_reg, password_reg
from repository.standard import standard_phone_number
from .serializers import UserLoginSerializer
from django.db.models import Q


@require_POST
def signup(request: HttpRequest):
    if 'username' not in request.POST and \
            'phone_number' not in request.POST and \
            'email' not in request.POST:
        return false_response(
            message=MESSAGE_4_AT_LEAST_THESE_FIELDS,
        )
    user_name = None
    if 'username' in request.POST:
        user_name = request.POST['username']
        if username_reg.match(user_name) is None:
            return false_response(
                message=MESSAGE_4_USERNAME_IS_INCORRECT,
            )
    phone_number = None
    if 'phone_number' in request.POST:
        phone_number = request.POST['phone_number']
        phone_number = standard_phone_number(phone_number)
        if phone_number is None:
            return false_response(
                message=MESSAGE_4_PHONENUMBER_IS_INCORRECT,
            )
    email_address = None
    if 'email' in request.POST:
        email_address = request.POST['email']
        if email_reg.match(email_address) is None:
            return false_response(
                message=MESSAGE_4_EMAIL_IS_INCORRECT,
            )
    if user_name is None:
        user_name = phone_number if phone_number is not None else email_address

    usr = User.objects.filter(
        Q(username=user_name) |
        Q(phone_number=phone_number) |
        Q(email=email_address)
    ).first()
    if usr is not None:
        return false_response(
            message=MESSAGE_4_USER_IS_EXIST,
        )

    if 'password' not in request.POST:
        return false_response(
            message=MESSAGE_4_PASSWORD_FIELD_IS_EMPTY,
        )
    password = request.POST['password']
    if password_reg.match(password) is None:
        return false_response(
            message=MESSAGE_4_PASSWORD_IS_INCORRECT,
        )
    usr = User()
    usr.username = user_name
    usr.email = email_address
    usr.phone_number = phone_number
    usr.password = password
    usr.save()
    return true_response(
        message=MESSAGE_4_USER_SIGNUP_SUCCESSFUL,
    )


@require_POST
def login(request: HttpRequest):
    if not request.user.is_anonymous:
        return false_response(
            message=MESSAGE_4_YOU_HAVE_BEEN_LOGGED_IN_BEFORE,
        )
    if 'username' not in request.POST:
        return false_response(
            message=MESSAGE_4_USERNAME_FIELD_IS_EMPTY,
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
        usr = User.objects.filter(email=request.POST['username']).first()
        if usr is not None:
            usr = authenticate(
                username=usr.username,
                password=request.POST['password']
            )
        if usr is None:
            usr = User.objects.filter(phone_number=request.POST['username']).first()
            if usr is not None:
                usr = authenticate(
                    username=usr.username,
                    password=request.POST['password']
                )
            if usr is None:
                return false_response(
                    message=MESSAGE_4_THERE_IS_NO_USER_WITH_THIS_PROFILE,
                )
    dj_login(request, usr)
    return true_response(
        message=MESSAGE_4_USER_LOGIN_SUCCESSFUL,
        data={
            'user': usr.to_dict(),
        }
    )


@require_GET
def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return true_response(
        message=MESSAGE_4_USER_LOGOUT_SUCCESSFUL,
    )
