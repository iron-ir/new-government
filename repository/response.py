from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound, JsonResponse


def false_response(message: str = None, data: dict = None):
    return JsonResponse(
        {
            'success': False,
            'message': message,
            'data': data,
        }
    )


def true_response(message: str = None, data: dict = None):
    return JsonResponse(
        {
            'success': True,
            'message': message,
            'data': data,
        }
    )
