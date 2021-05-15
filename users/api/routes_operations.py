from repository.messages import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from users.models import User, UserRole


def login(username, password, request, *args, **kwargs):
    usr = authenticate(username=username, password=password)
    if usr is None:
        raise Exception(MESSAGE_4_AUTHENTICATE_FAIL)
    dj_login(request, usr)
    return {
        'user': {
            'id': usr.id,
        },
    }


def get_users_by_role_and_place(role, place, request, *args, **kwargs):
    return {}


def get_users_by_role(role_id, request, *args, **kwargs):
    users_role = UserRole.objects.filter(role_id=role_id).all()
    users_to_dict = {}
    for urole in users_role:
        users_to_dict[urole.user.id] = urole.user.to_dict()
    return {'users_list': users_to_dict}


def get_all_users(request, *args, **kwargs):
    users = User.objects.all()
    # todo
    return {}
