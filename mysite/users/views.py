from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

from .repository.regular_expression import (
    username_reg,
    password_reg,
    nationalcode_reg
)
from .repository.validators import permitted_age
from .models import User as MyUser


@login_required
@require_GET
def index(request: HttpRequest):
    return render(request, 'users/index.html')


@require_GET
def singup_form(request: HttpRequest):
    return render(request, 'users/signup.html')


@require_POST
def singup_done(request: HttpRequest):
    if 'birthday' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به تاریخ تولد خالی است.')
        return redirect('users:signup_form')
    if 'nationalcode' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به شماره ملی خالی است.')
        return redirect('users:signup_form')
    if 'username' not in request.POST:
        request.POST['username'] = request.POST['nationalcode']
    if 'password' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به کلمه عبور خالی است.')
        return redirect('users:signup_form')
    if 'confirm_password' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به تایید کلمه عبور خالی است.')
        return redirect('users:signup_form')
    if 'first_name' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به نام خالی است.')
        return redirect('users:signup_form')
    if 'last_name' not in request.POST:
        messages.add_message(request, messages.INFO, 'فیلد مربوط به نام خانوادگی خالی است.')
        return redirect('users:signup_form')

    birthday = request.POST['birthday']
    if permitted_age(birthday) is False:
        messages.add_message(request, messages.ERROR, 'شما برای شرکت در انتخابات پیشرو به سن مجاز نرسیده اید.')
        return redirect('users:signup_form')

    nationalcode = request.POST['nationalcode']
    if MyUser.objects.filter(nationalcode=nationalcode).first():
        messages.add_message(request, messages.ERROR, "کاربر با این شماره ملی قبلا ثبت نام شده است،"
                                                      "درصورت ثبت شکایت با پشتیبانی سایت تماس بگیرید.")
        return redirect('users:signup_form')
    if nationalcode_reg.match(nationalcode) is None:
        messages.add_message(request, messages.ERROR, 'فرمت شماره ملی رعایت نشده است.')
        return redirect('users:signup_form')

    username = request.POST['username']
    if MyUser.objects.filter(username=username).first():
        messages.add_message(request, messages.ERROR, 'کاربر با این نام کاربری موجود می باشد.')
        return redirect('users:signup_form')
    if username_reg.match(username) is None:
        messages.add_message(request, messages.ERROR, 'فرمت نام کاربری رعایت نشده است.')
        return redirect('users:signup_form')

    password = request.POST['password']
    if password_reg.match(password) is None:
        messages.add_message(request, messages.ERROR, 'حداقل طول کلمه عبور هشت کاراکتر می باشد.')
        return redirect('users:signup_form')
    confirm_password = request.POST['confirm_password']
    if password != confirm_password:
        messages.add_message(request, messages.ERROR, 'کلمه عبور و تایید کلمه عبور با یکدیگر یکسان نمی باشند.')
        return redirect('users:signup_form')

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    usr = MyUser()
    usr.birthday = birthday
    usr.nationalcode = nationalcode
    usr.username = username
    usr.password = make_password(password)
    usr.first_name = first_name
    usr.last_name = last_name
    usr.save()
    return redirect('users:login_form')


@require_GET
def login_form(request: HttpRequest):
    if request.user.is_anonymous:
        return render(request, 'users/login.html')
    return redirect('users:index')


@require_POST
def login_done(request: HttpRequest):
    if not request.user.is_anonymous:
        return redirect('users:index')
    if 'username' not in request.POST:
        messages.add_message(request, messages.ERROR, 'شماره ملی/نام کاربری خود را وارد کنید.')
        return redirect('users:login_form')

    if 'password' not in request.POST:
        messages.add_message(request, messages.ERROR, 'کلمه عبور خود را وارد کنید.')
        return redirect('users:login_form')

    usr = authenticate(username=request.POST['username'],
                       password=request.POST['password'])
    if usr is None:
        usr = authenticate(nationalcode=request.POST['username'],
                           password=request.POST['password'])
    if usr is None:
        messages.add_message(request, messages.ERROR, 'شماره ملی/نام کاربری یا کلمه عبور اشتباه است.')
        return redirect('users:login_form')
    dj_login(request, usr)
    return redirect('users:index')


@login_required
@require_GET
def logout_form(request: HttpRequest):
    return render(request, 'users/logout.html')


@login_required
@require_POST
def logout_done(request: HttpRequest):
    dj_logout(request)
    return redirect('users:login_form')

#
# @login_required
# @require_GET
# def password_reset_form(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
#
#
# @login_required
# @require_POST
# def password_reset_done(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
#
#
# @login_required
# @require_GET
# def delete_account_form(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
#
#
# @login_required
# @require_POST
# def delete_account_done(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
#
#
# @require_GET
# def vcode_form(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
#
#
# @require_POST
# def vcode_done(request: HttpRequest):
#     return JsonResponse(
#         {
#             'success': True,
#             'message': [],
#             'data': [],
#         }
#     )
