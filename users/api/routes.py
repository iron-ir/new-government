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
from repository.standard import *
from repository.messages import *
from repository.definitions import *
from repository.regular_expression import username_reg, email_reg, password_reg, nationalcode_reg
from repository.functions import send_sms_vcode, send_email_vcode
from .serializers import UserLoginSerializer
from django.db.models import Q
from users.models import create_vcode, vcode_is_acceptable
from users.models import all_user_information, WorkExpiration, EducationHistory, Standpoint, Effect, UserRelation


@require_POST
def signup(request: HttpRequest):
    if 'username' not in request.POST and \
            'phone_number' not in request.POST and \
            'email' not in request.POST:
        return false_response(
            message=MESSAGE_4_AT_LEAST_THESE_FIELDS,
        )
    i = 0
    if 'username' in request.POST:
        if 0 == len(request.POST['username']):
            i += 1
    if 'phone_number' in request.POST:
        if 0 == len(request.POST['phone_number']):
            i += 1
    if 'email' in request.POST:
        if 0 == len(request.POST['email']):
            i += 1
    if i == 3:
        return false_response(
            message=MESSAGE_4_AT_LEAST_THESE_FIELDS,
        )
    user_name = None
    if 'username' in request.POST:
        if len(request.POST['username']) != 0:
            user_name = request.POST['username']
            if username_reg.match(user_name) is None:
                return false_response(
                    message=MESSAGE_4_USERNAME_IS_INCORRECT,
                )
            usr = User.objects.filter(username=user_name).first()
            if usr is not None:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
    phone_number = None
    if 'phone_number' in request.POST:
        if len(request.POST['phone_number']) != 0:
            phone_number = request.POST['phone_number']
            phone_number = standard_phone_number(phone_number)
            if phone_number is None:
                return false_response(
                    message=MESSAGE_4_PHONENUMBER_IS_INCORRECT,
                )
            usr = User.objects.filter(phone_number=phone_number).first()
            if usr is not None:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
    email_address = None
    if 'email' in request.POST:
        if len(request.POST['email']) != 0:
            email_address = request.POST['email']
            if email_reg.match(email_address) is None:
                return false_response(
                    message=MESSAGE_4_EMAIL_IS_INCORRECT,
                )
            usr = User.objects.filter(email=email_address).first()
            if usr is not None:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
        if user_name is None:
            user_name = phone_number if phone_number is not None else email_address
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
        if len(request.POST['username']) != 0:
            user_name = request.POST['username']
            if username_reg.match(user_name) is None:
                return false_response(
                    message=MESSAGE_4_USERNAME_IS_INCORRECT,
                )
            last_usr = User.objects.filter(username=user_name).first()
            if last_usr is not None and last_usr != request.user:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
            usr.username = user_name
    if 'phone_number' in request.POST:
        if len(request.POST['phone_number']) != 0:
            phone_number = request.POST['phone_number']
            phone_number = standard_phone_number(phone_number)
            if phone_number is None:
                return false_response(
                    message=MESSAGE_4_PHONENUMBER_IS_INCORRECT,
                )
            last_usr = User.objects.filter(phone_number=phone_number).first()
            if last_usr is not None and last_usr != request.user:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
            if phone_number != usr.phone_number:
                usr.is_phone_number_verify = False
                usr.phone_number = phone_number
    if 'email' in request.POST:
        if len(request.POST['email']) != 0:
            email_address = request.POST['email']
            if email_reg.match(email_address) is None:
                return false_response(
                    message=MESSAGE_4_EMAIL_IS_INCORRECT,
                )
            last_usr = User.objects.filter(email=email_address).first()
            if last_usr is not None and last_usr != request.user:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
            if email_address != usr.email:
                usr.is_email_verify = False
                usr.email = email_address
    if 'password' in request.POST:
        if len(request.POST['password']) != 0:
            password = request.POST['password']
            if password_reg.match(password) is None:
                return false_response(
                    message=MESSAGE_4_PASSWORD_IS_INCORRECT,
                )
            usr.password = password
    if 'avatar' in request.POST:
        if len(request.POST['avatar']) != 0:
            usr.avatar = standard_avatar(request.POST['avatar'])
    if 'first_name' in request.POST:
        if len(request.POST['first_name']) != 0:
            if usr.first_name != request.POST['first_name']:
                usr.is_personal_information_verify = False
                usr.first_name = request.POST['first_name']
    if 'last_name' in request.POST:
        if len(request.POST['last_name']) != 0:
            if usr.last_name != request.POST['last_name']:
                usr.is_personal_information_verify = False
                usr.last_name = request.POST['last_name']
    if 'gender' in request.POST:
        if len(request.POST['gender']) != 0:
            if usr._gender != standard_gender(request.POST['gender']):
                usr.is_personal_information_verify = False
                usr.gender = standard_gender(request.POST['gender'])
    if 'national_code' in request.POST:
        if len(request.POST['national_code']) != 0:
            national_code = request.POST['national_code']
            if nationalcode_reg.match(national_code) is None:
                return false_response(
                    message=MESSAGE_4_NATIONALCODE_IS_INCORRECT,
                )
            last_usr = User.objects.filter(national_code=national_code).first()
            if last_usr is not None and last_usr != request.user:
                return false_response(
                    message=MESSAGE_4_USER_IS_EXIST,
                )
            if usr.national_code != national_code:
                usr.is_personal_information_verify = False
                usr.national_code = national_code
    if 'father_name' in request.POST:
        if len(request.POST['father_name']) != 0:
            if usr.father_name != request.POST['father_name']:
                usr.is_personal_information_verify = False
                usr.father_name = request.POST['father_name']
    if 'mother_name' in request.POST:
        if len(request.POST['mother_name']) != 0:
            if usr.mother_name != request.POST['mother_name']:
                usr.is_personal_information_verify = False
                usr.mother_name = request.POST['mother_name']
    if 'birth_date' in request.POST:
        if len(request.POST['birth_date']) != 0:
            birth_date = standard_birth_date(request.POST['birth_date'])
            if usr.birth_date != birth_date:
                usr.is_personal_information_verify = False
                usr.birth_date = birth_date
    if 'birth_place_id' in request.POST:
        if len(request.POST['birth_place_id']) != 0:
            birth_place = standard_birth_place(request.POST['birth_place_id'])
            if usr.birth_place != birth_place:
                usr.is_personal_information_verify = False
                usr.birth_place = birth_place
    if 'nationality_id' in request.POST:
        if len(request.POST['nationality_id']) != 0:
            nationality = standard_nationality(request.POST['nationality_id'])
            if usr.nationality != nationality:
                usr.is_personal_information_verify = False
                usr.nationality = nationality
    if 'religion_id' in request.POST:
        if len(request.POST['religion_id']) != 0:
            religion = standard_religion(request.POST['religion_id'])
            if usr.religion != religion:
                usr.is_personal_information_verify = False
                usr.religion = religion
    if 'official_website' in request.POST:
        if len(request.POST['official_website']) != 0:
            official_website = standard_official_website(request.POST['official_website'])
            if usr.official_website != official_website:
                usr.is_personal_information_verify = False
                usr.official_website = official_website

    usr.save()
    return true_response(
        message=MESSAGE_4_USER_UPDATE_SUCCESSFUL,
        data={
            'user': usr.to_dict()
        }
    )


@require_GET
@login_required
def sms_vcode(request: HttpRequest):
    if request.user.phone_number is None:
        return false_response(
            message=MESSAGE_4_PHONE_NUMBER_NOT_EXIST,
        )
    res = send_sms_vcode(
        vcode=create_vcode(user=request.user, vtype=PHONE_NUMBER),
        phone_number=request.user.phone_number,
    )
    if not res:
        return false_response(
            message=MESSAGE_4_VCODE_SMS_FAIL,
        )
    return true_response(
        message=MESSAGE_4_VCODE_SMS,
    )


@require_GET
@login_required
def email_vcode(request: HttpRequest):
    if request.user.email is None:
        return false_response(
            message=MESSAGE_4_EMAIL_NOT_EXIST,
        )
    res = send_email_vcode(
        vcode=create_vcode(user=request.user, vtype=EMAIL_ADDRESS),
        email=request.user.email,
    )
    if not res:
        return false_response(
            message=MESSAGE_4_VCODE_EMAIL_FAIL,
        )
    return true_response(
        message=MESSAGE_4_VCODE_EMAIL,
    )


@require_POST
@login_required
def confirm_phone_number(request: HttpRequest):
    if 'code' not in request.POST:
        return false_response(
            message=MESSAGE_4_VCODE_PHONE_NUMBER_FIELD_IS_EMPTY,
        )
    if len(request.POST['code']) == 0:
        return false_response(
            message=MESSAGE_4_VCODE_PHONE_NUMBER_FIELD_IS_EMPTY,
        )
    res = vcode_is_acceptable(
        code=request.POST['code'],
        user=request.user,
        vtype=PHONE_NUMBER,
    )
    if not res:
        return false_response(
            message=MESSAGE_4_VCODE_PHONE_NUMBER_IS_NOT_VALID,
        )
    request.user.is_phone_number_verify = True
    request.user.save()
    return true_response(
        message=MESSAGE_4_VCODE_PHONE_NUMBER_IS_VALID,
    )


@require_POST
@login_required
def confirm_email_address(request: HttpRequest):
    if 'code' not in request.POST:
        return false_response(
            message=MESSAGE_4_VCODE_EMAIL_FIELD_IS_EMPTY,
        )
    if len(request.POST['code']) == 0:
        return false_response(
            message=MESSAGE_4_VCODE_EMAIL_FIELD_IS_EMPTY,
        )
    res = vcode_is_acceptable(
        code=request.POST['code'],
        user=request.user,
        vtype=EMAIL_ADDRESS,
    )
    if not res:
        return false_response(
            message=MESSAGE_4_VCODE_EMAIL_IS_NOT_VALID,
        )
    request.user.is_email_verify = True
    request.user.save()
    return true_response(
        message=MESSAGE_4_VCODE_EMAIL_IS_VALID,
    )


@require_GET
@login_required
def get_all_user_information(request: HttpRequest):
    return true_response(
        data=all_user_information(user=request.user),
    )


@require_POST
@login_required
def add_work_expiration(request: HttpRequest):
    place_number_for_sorting = None
    if 'place_number_for_sorting' in request.POST:
        if len(request.POST['place_number_for_sorting']) != 0:
            place_number_for_sorting = int(request.POST['place_number_for_sorting'])
    if 'post_title' not in request.POST:
        return false_response(
            message=MESSAGE_4_POST_TITLE_FIELD_IS_EMPTY,
        )
    if len(request.POST['post_title']) == 0:
        return false_response(
            message=MESSAGE_4_POST_TITLE_FIELD_IS_EMPTY,
        )
    post_title = request.POST['post_title']
    cooperation_type_id = None
    if 'cooperation_type_id' in request.POST:
        if len(request.POST['cooperation_type_id']) != 0:
            cooperation_type_id = standard_base_information_obj(request.POST['cooperation_type_id'])
    from_date = None
    if 'from_date' in request.POST:
        if len(request.POST['from_date']) != 0:
            from_date = standard_date(request.POST['from_date'])
    to_date = None
    if 'to_date' in request.POST:
        if len(request.POST['to_date']) != 0:
            to_date = standard_date(request.POST['to_date'])
    activity_type_id = None
    if 'activity_type_id' in request.POST:
        if len(request.POST['activity_type_id']) != 0:
            activity_type_id = standard_base_information_obj(request.POST['activity_type_id'])
    organization_name = None
    if 'organization_name' in request.POST:
        if len(request.POST['organization_name']) != 0:
            organization_name = request.POST['organization_name']

    work_expiration = WorkExpiration()
    work_expiration.user = request.user
    work_expiration.place_number_for_sorting = place_number_for_sorting
    work_expiration.post_title = post_title
    work_expiration.cooperation_type_id = cooperation_type_id
    work_expiration.from_date = from_date
    work_expiration.to_date = to_date
    work_expiration.activity_type_id = activity_type_id
    work_expiration.organization_name = organization_name
    work_expiration.save()

    return true_response(
        message=MESSAGE_4_WORK_EXPIRATION_REGISTERD,
    )


@require_POST
@login_required
def add_education_history(request: HttpRequest):
    place_number_for_sorting = None
    if 'place_number_for_sorting' in request.POST:
        if len(request.POST['place_number_for_sorting']) != 0:
            place_number_for_sorting = int(request.POST['place_number_for_sorting'])
    if 'degree_type_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_DEGREE_TYPE_FIELD_IS_EMPTY,
        )
    if len(request.POST['degree_type_id']) == 0:
        return false_response(
            message=MESSAGE_4_DEGREE_TYPE_FIELD_IS_EMPTY,
        )
    degree_type = standard_base_information_obj(request.POST['degree_type_id'])
    if degree_type is None:
        return false_response(
            message=MESSAGE_4_DEGREE_TYPE_FIELD_IS_EMPTY,
        )
    if 'field_of_study_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_FEILD_OF_STADY_FIELD_IS_EMPTY,
        )
    if len(request.POST['field_of_study_id']) == 0:
        return false_response(
            message=MESSAGE_4_FEILD_OF_STADY_FIELD_IS_EMPTY,
        )
    field_of_study = standard_base_information_obj(request.POST['field_of_study_id'])
    if field_of_study is None:
        return false_response(
            message=MESSAGE_4_FEILD_OF_STADY_FIELD_IS_EMPTY,
        )
    if 'place_of_study_type_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_PLACE_OF_STADY_TYPE_FIELD_IS_EMPTY,
        )
    if len(request.POST['place_of_study_type_id']) == 0:
        return false_response(
            message=MESSAGE_4_PLACE_OF_STADY_TYPE_FIELD_IS_EMPTY,
        )
    place_of_study_type = standard_base_information_obj(request.POST['place_of_study_type_id'])
    if place_of_study_type is None:
        return false_response(
            message=MESSAGE_4_PLACE_OF_STADY_TYPE_FIELD_IS_EMPTY,
        )
    if 'place_of_study' not in request.POST:
        return false_response(
            message=MESSAGE_4_PLACE_OF_STADY_FIELD_IS_EMPTY,
        )
    if len(request.POST['place_of_study']) == 0:
        return false_response(
            message=MESSAGE_4_PLACE_OF_STADY_FIELD_IS_EMPTY,
        )
    place_of_study = request.POST['place_of_study']
    if 'zone_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_ZONE_FIELD_IS_EMPTY,
        )
    if len(request.POST['zone_id']) == 0:
        return false_response(
            message=MESSAGE_4_ZONE_FIELD_IS_EMPTY,
        )
    zone = standard_zone(request.POST['zone_id'])
    if zone is None:
        return false_response(
            message=MESSAGE_4_ZONE_FIELD_IS_EMPTY,
        )
    graduation_date = None
    if 'graduation_date' in request.POST:
        if len(request.POST['graduation_date']) != 0:
            graduation_date = standard_date(request.POST['graduation_date'])
    is_study = False
    if 'is_study' in request.POST:
        if len(request.POST['is_study']) != 0:
            is_study = standard_bool(request.POST['is_study'])

    education_history = EducationHistory()
    education_history.place_number_for_sorting = place_number_for_sorting
    education_history.user = request.user
    education_history.degree_type = degree_type
    education_history.field_of_study = field_of_study
    education_history.place_of_study_type = place_of_study_type
    education_history.place_of_study = place_of_study
    education_history.zone = zone
    education_history.graduation_date = graduation_date
    education_history.is_study = is_study

    education_history.save()

    return true_response(
        message=MESSAGE_4_EDUCATION_HISTORY_REGISTERD,
    )


@require_POST
@login_required
def add_standpoint(request: HttpRequest):
    place_number_for_sorting = None
    if 'place_number_for_sorting' in request.POST:
        if len(request.POST['place_number_for_sorting']) != 0:
            place_number_for_sorting = int(request.POST['place_number_for_sorting'])

    if 'group_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_GROUP_FIELD_IS_EMPTY,
        )
    if len(request.POST['group_id']) == 0:
        return false_response(
            message=MESSAGE_4_GROUP_FIELD_IS_EMPTY,
        )
    group = standard_base_information_obj(request.POST['group_id'])
    if group is None:
        return false_response(
            message=MESSAGE_4_GROUP_FIELD_IS_EMPTY,
        )

    if 'title' not in request.POST:
        return false_response(
            message=MESSAGE_4_TITLE_FIELD_IS_EMPTY,
        )
    if len(request.POST['title']) == 0:
        return false_response(
            message=MESSAGE_4_TITLE_FIELD_IS_EMPTY,
        )
    title = request.POST['title']
    description = None
    if 'description' in request.POST:
        if len(request.POST['description']) != 0:
            description = request.POST['description']
    link = None
    if 'link_url' in request.POST:
        if len(request.POST['link_url']) != 0:
            link = standard_url(request.POST['link_url'])
    attachment = None
    if 'attachment_path' in request.POST:
        if len(request.POST['attachment_path']) != 0:
            attachment = standard_file(request.POST['attachment_path'])

    standpoint = Standpoint()
    standpoint.place_number_for_sorting = place_number_for_sorting
    standpoint.user = request.user
    standpoint.group = group
    standpoint.title = title
    standpoint.description = description
    standpoint.link = link
    standpoint.attachment = attachment
    standpoint.save()

    return true_response(
        message=MESSAGE_4_STANDPOINT_REGISTERD,
    )


@require_POST
@login_required
def add_effect(request: HttpRequest):
    place_number_for_sorting = None
    if 'place_number_for_sorting' in request.POST:
        if len(request.POST['place_number_for_sorting']) != 0:
            place_number_for_sorting = int(request.POST['place_number_for_sorting'])

    if 'type_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_TYPE_FIELD_IS_EMPTY,
        )
    if len(request.POST['type_id']) == 0:
        return false_response(
            message=MESSAGE_4_TYPE_FIELD_IS_EMPTY,
        )
    etype = standard_base_information_obj(request.POST['type_id'])
    if etype is None:
        return false_response(
            message=MESSAGE_4_TYPE_FIELD_IS_EMPTY,
        )
    if 'title' not in request.POST:
        return false_response(
            message=MESSAGE_4_TITLE_FIELD_IS_EMPTY,
        )
    if len(request.POST['title']) == 0:
        return false_response(
            message=MESSAGE_4_TITLE_FIELD_IS_EMPTY,
        )
    title = request.POST['title']
    description = None
    if 'description' in request.POST:
        if len(request.POST['description']) != 0:
            description = request.POST['description']
    link = None
    if 'link_url' in request.POST:
        if len(request.POST['link_url']) != 0:
            link = standard_url(request.POST['link_url'])
    attachment = None
    if 'attachment_path' in request.POST:
        if len(request.POST['attachment_path']) != 0:
            attachment = standard_file(request.POST['attachment_path'])

    effect = Effect()
    effect.place_number_for_sorting = place_number_for_sorting
    effect.user = request.user
    effect.etype = etype
    effect.title = title
    effect.description = description
    effect.link = link
    effect.attachment = attachment
    effect.save()

    return true_response(
        message=MESSAGE_4_EFFECT_REGISTERD,
    )


@require_POST
@login_required
def add_user_relation(request: HttpRequest):
    if 'related_user_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_RELATED_USER_FIELD_IS_EMPTY,
        )
    if len(request.POST['related_user_id']) == 0:
        return false_response(
            message=MESSAGE_4_RELATED_USER_FIELD_IS_EMPTY,
        )
    related_user = standard_user(request.POST['related_user_id'])
    if related_user is None:
        return false_response(
            message=MESSAGE_4_RELATED_USER_FIELD_IS_EMPTY,
        )
    if request.user == related_user:
        return false_response(
            message=MESSAGE_4_USER_WITH_USER,
        )
    if UserRelation.objects.filter(base_user=request.user).filter(related_user=related_user).first() or \
            UserRelation.objects.filter(related_user=request.user).filter(base_user=related_user).first():
        return false_response(
            message=MESSAGE_4_RELATED,
        )

    if 'type_id' not in request.POST:
        return false_response(
            message=MESSAGE_4_RELATED_TYPE_FIELD_IS_EMPTY,
        )
    if len(request.POST['type_id']) == 0:
        return false_response(
            message=MESSAGE_4_RELATED_TYPE_FIELD_IS_EMPTY,
        )
    rtype = standard_base_information_obj(request.POST['type_id'])
    if rtype is None:
        return false_response(
            message=MESSAGE_4_RELATED_TYPE_FIELD_IS_EMPTY,
        )
    form_date = None
    if 'form_date' in request.POST:
        if len(request.POST['form_date']) != 0:
            form_date = standard_date(request.POST['form_date'])
    to_date = None
    if 'to_date' in request.POST:
        if len(request.POST['to_date']) != 0:
            to_date = standard_date(request.POST['to_date'])

    user_relation = UserRelation()

    user_relation.base_user = request.user
    user_relation.base_user_verification = True
    user_relation.related_user = related_user
    user_relation.rtype = rtype
    user_relation.form_date = form_date
    user_relation.to_date = to_date

    user_relation.save()

    # todo dadane payam b farde dar rabete baraye taeide rabete.

    return true_response(
        message=MESSAGE_4_USER_RELATION_REGISTERD,
    )

# @require_POST
# @login_required
# def verification_of_information(request: HttpRequest):
#     usr = request.user
#     if usr.is_candidate:
#         if usr.is_suspension:
#             return false_response(
#                 message=MESSAGE_4_YOU_SUSPENDION
#             )
#         else:
#             return true_response(
#                 message=MESSAGE_4_YOU_CANDIDATE
#             )
#     if not usr.is_personal_information_verify:
#         return false_response(
#             message=YOUR_PROFILE_INFORMATION_IS_INCOMPLETE,
#         )
#     from users.models import EducationHistory, WorkExpiration
#     if EducationHistory.objects.filter(user=usr).all() is None:
#         return false_response(
#             message=YOUR_PROFILE_INFORMATION_IS_INCOMPLETE,
#         )
#     if WorkExpiration.objects.filter(user=usr).all() is None:
#         return false_response(
#             message=YOUR_PROFILE_INFORMATION_IS_INCOMPLETE,
#         )
#
#     cndd = Candidate()
#     cndd.user = usr
#     cndd.save()
#     return true_response(
#         message=MESSAGE_4_YOU_CANDIDATE
#     )
