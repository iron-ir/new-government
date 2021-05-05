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
from repository.regular_expression import username_reg, email_reg, password_reg, nationalcode_reg
from repository.standard import standard_phone_number, standard_gender, standard_birth_date, standard_birth_place, \
    standard_official_website, standard_avatar
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


@require_POST
@login_required
def update(request: HttpRequest):
    usr = request.user
    if 'username' in request.POST:
        user_name = request.POST['username']
        if username_reg.match(user_name) is None:
            return false_response(
                message=MESSAGE_4_USERNAME_IS_INCORRECT,
            )
        last_usr = User.objects.filter(username=usr.username).first()
        if last_usr is not None:
            return false_response(
                message=MESSAGE_4_USER_IS_EXIST,
            )
        usr.username = user_name
    if 'phone_number' in request.POST:
        phone_number = request.POST['phone_number']
        phone_number = standard_phone_number(phone_number)
        if phone_number is None:
            return false_response(
                message=MESSAGE_4_PHONENUMBER_IS_INCORRECT,
            )
        last_usr = User.objects.filter(phone_number=usr.phone_number).first()
        if last_usr is not None:
            return false_response(
                message=MESSAGE_4_USER_IS_EXIST,
            )
        usr.phone_number = phone_number
    if 'email' in request.POST:
        email_address = request.POST['email']
        if email_reg.match(email_address) is None:
            return false_response(
                message=MESSAGE_4_EMAIL_IS_INCORRECT,
            )
        last_usr = User.objects.filter(email=usr.email).first()
        if last_usr is not None:
            return false_response(
                message=MESSAGE_4_USER_IS_EXIST,
            )
        usr.email = email_address
    if 'password' in request.POST:
        password = request.POST['password']
        if password_reg.match(password) is None:
            return false_response(
                message=MESSAGE_4_PASSWORD_IS_INCORRECT,
            )
        usr.password = password
    if 'avatar' in request.POST:
        usr.avatar = standard_avatar(request.POST['avatar'])
    if 'first_name' in request.POST:
        usr.first_name = request.POST['first_name']
    if 'last_name' in request.POST:
        usr.last_name = request.POST['last_name']
    if 'last_name' in request.POST:
        usr.last_name = request.POST['last_name']
    if 'gender' in request.POST:
        usr.gender = standard_gender(request.POST['gender'])
    if 'national_code' in request.POST:
        national_code = request.POST['national_code']
        if nationalcode_reg.match(national_code) is None:
            return false_response(
                message=MESSAGE_4_NATIONALCODE_IS_INCORRECT,
            )
        usr.national_code = national_code
    if 'father_name' in request.POST:
        usr.father_name = request.POST['father_name']
    if 'mother_name' in request.POST:
        usr.mother_name = request.POST['mother_name']
    if 'birth_date' in request.POST:
        usr.birth_date = standard_birth_date(request.POST['birth_date'])
    if 'birth_place_code' in request.POST:
        usr.birth_place = standard_birth_place(request.POST['birth_place_code'])
    if 'nationality' in request.POST:
        usr.nationality = request.POST['nationality']
    if 'religion' in request.POST:
        usr.religion = request.POST['religion']
    if 'official_website' in request.POST:
        usr.official_website = standard_official_website(request.POST['religion'])

    usr.save()
    return true_response(
        message=MESSAGE_4_USER_UPDATE_SUCCESSFUL,
        data={
            'user': usr.to_dict()
        }
    )
