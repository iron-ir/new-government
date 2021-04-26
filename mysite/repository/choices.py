YES_OR_NO_CHOICES = (
    (False, 'خیر'),
    (True, 'بله'),
)


def YES_OR_NO_RETURNER(value):
    if value is True:
        return 'بله'
    if value is False:
        return 'خیر'
    return 'نامعلوم'


GENDER_CHOICES = (
    ('0', 'خانوم'),
    ('1', 'آقا'),
)
GENDER_DEFAULT = '1'


def GENDER_RETURNER(value):
    if value == '0':
        return 'خانوم'
    if value == '1':
        return 'آقا'
    return 'نامعلوم'


VCODE_CHOICES = (
    ('1', 'phone_number'),
    ('2', 'email_address'),
)
VCODE_DEFAULT = '1'

