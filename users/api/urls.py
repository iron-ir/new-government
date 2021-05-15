from django.contrib.auth.decorators import login_required

from django.urls import path, include
from . import routes

app_name = 'users'

urlpatterns = [
    path('signup', routes.signup_route),
    path('login', routes.login_route),
    path('logout', routes.logout_route),
    path('update', routes.update_route),
    path('sms/vcode', routes.sms_vcode_route),
    path('email/vcode', routes.email_vcode_route),
    path('confirm/phone/number', routes.confirm_phone_number_route),
    path('confirm/email/address', routes.confirm_email_address_route),
    path('get/all/user/information', routes.get_all_user_information_route),
    path('add/work/expiration', routes.add_work_expiration_route),
    path('add/education/history', routes.add_education_history_route),
    path('add/standpoint', routes.add_standpoint_route),
    path('add/effect', routes.add_effect_route),
    path('add/user/relation', routes.add_user_relation_route),

    # path('candidate/verify/info/', routes.verification_of_information)
]
