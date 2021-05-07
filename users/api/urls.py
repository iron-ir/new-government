from django.contrib.auth.decorators import login_required

from django.urls import path, include
from . import routes

app_name = 'users'

urlpatterns = [
    path('signup', routes.signup),
    path('login', routes.login),
    path('logout', routes.logout),
    path('update', routes.update),
    path('sms/vcode', routes.sms_vcode),
    path('email/vcode', routes.email_vcode),
    path('confirm/phone/number', routes.confirm_phone_number),
    path('confirm/email/address', routes.confirm_email_address),
    path('get/all/user/information', routes.get_all_user_information),
    path('add/work/expiration', routes.add_work_expiration),
    path('add/education/history', routes.add_education_history),
    path('add/standpoint', routes.add_standpoint),
    path('add/effect', routes.add_effect),
    path('add/user/relation', routes.add_user_relation),

    # path('candidate/verify/info/', routes.verification_of_information)
]
