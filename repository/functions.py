from functools import wraps
from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound, JsonResponse
from repository.manage_data_rules import law_enforcement_manager


def send_sms_vcode(vcode: str, phone_number: str) -> bool:
    return True


def send_email_vcode(vcode: str, email: str) -> bool:
    return True


def input_output_management(rules):
    def decorator(function):
        @wraps(function)
        def wrap(request: HttpRequest, *args, **kwargs):
            try:
                data = law_enforcement_manager(rules.INPUT, request.POST)
                result = function(request, data, *args, **kwargs)
                # todo _output = data_cleaner(result, rule['output'])
                return JsonResponse({
                    'success': True,
                    'message': None,
                    'data': result,
                })

            except Exception as ex:
                return JsonResponse({
                    'success': False,
                    'message': ex.args,
                    'data': None,
                })

        return wrap

    return decorator
