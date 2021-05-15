from repository.messages import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login


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
