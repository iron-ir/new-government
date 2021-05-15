from django.views.decorators.http import require_POST, require_GET
from django.http import HttpRequest

from repository.functions import input_output_management

from . import rules
from . import routes_operations as opr


@require_POST
@input_output_management(rules.GET_USERS_RULES)
def get_users_route(request: HttpRequest, data: dict, *args, **kwargs):
    print(data)
    if 'place_id' in data['user_role']:
        res = opr.get_users_by_role_and_place(data['user_role']['role_id'], data['user_role']['place_id'], request,
                                              *args, **kwargs)

    elif 'role_id' in data['user_role']:
        res = opr.get_users_by_role(data['user_role']['role_id'], request, *args, **kwargs)

    else:
        res = opr.get_all_users(request, *args, **kwargs)

    return res
