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
    ('0', 'خالی'),
    ('1', 'خانوم'),
    ('2', 'آقا'),
    ('3', 'دیگر'),
)
GENDER_DEFAULT = '0'


def GENDER_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'خانوم'
    if value == '2':
        return 'آقا'
    if value == '3':
        return 'دیگر'

    return 'نامعلوم'


VCODE_CHOICES = (
    ('1', 'phone_number'),
    ('2', 'email_address'),
)
VCODE_DEFAULT = '1'

DEGREE_TYPE_CHOICES = (
    ('0', 'خالی'),
    ('1', 'متوسطه'),
    ('2', 'کاردانی'),
    ('3', 'کارشناس'),
    ('4', 'کارشناسی ارشد'),
    ('5', 'دکتری'),
    ('6', 'دکتری تخصصی'),
)
DEGREE_TYPE_DEFAULT = '0'


def DEGREE_TYPE_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'متوسطه'
    if value == '2':
        return 'کاردانی'
    if value == '3':
        return 'کارشناسی'
    if value == '4':
        return 'کارشناسی ارشد'
    if value == '5':
        return 'دکتری'
    if value == '6':
        return 'دکتری تخصصی'

    return 'نامعلوم'


PLACE_OF_STUDY_TYPE_CHOICES = (
    ('0', 'خالی'),
    ('1', 'دولتی-روزانه'),
    ('2', 'دولتی-شبانه'),
    ('3', 'دولتی-پردیس'),
    ('4', 'آزاد اسلامی'),
    ('5', 'غیرانتفاعی'),
    ('6', 'پیام نور'),
    ('7', 'مراکز دیگر'),

)
PLACE_OF_STUDY_TYPE_DEFAULT = '0'


def PLACE_OF_STUDY_TYPE_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'دولتی-روزانه'
    if value == '2':
        return 'دولتی-شبانه'
    if value == '3':
        return 'دولتی-پردیس'
    if value == '4':
        return 'آزاد اسلامی'
    if value == '5':
        return 'پیام نور'
    if value == '6':
        return 'مراکز دیگر'

    return 'نامعلوم'


ZONE_TYPE_CHOICES = (
    ('0', 'خالی'),
    ('1', 'کشور'),
    ('2', 'استان'),
    ('3', 'شهرستان'),
    ('4', 'شهر'),
    ('5', 'بخش'),
    ('6', 'دهستان'),
    ('7', 'ده'),
    ('8', 'منطقه'),
    ('9', 'محله'),

)
ZONE_TYPE_DEFAULT = '0'


def ZONE_TYPE_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'کشور'
    if value == '2':
        return 'استان'
    if value == '3':
        return 'شهرستان'
    if value == '4':
        return 'شهر'
    if value == '5':
        return 'بخش'
    if value == '6':
        return 'دهستان'
    if value == '7':
        return 'ده'
    if value == '8':
        return 'منطقه'
    if value == '9':
        return 'محله'

    return 'نامعلوم'


COOPERATION_TYPE_CHOICES = (
    ('0', 'خالی'),
    ('1', 'پاره وقت'),
    ('2', 'تمام وقت'),
    ('3', 'مشاوره'),
)

COOPERATION_TYPE_DEFAULT = '0'


def COOPERATION_TYPE_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'پاره وقت'
    if value == '2':
        return 'تمام وقت'
    if value == '3':
        return 'مشاوره'

    return 'نامعلوم'


ACTIVITY_TYPE_CHOICES = (
    ('0', 'خالی'),
    ('1', 'قراردادی'),
    ('2', 'پیمانی'),
    ('3', 'رسمی'),
)

ACTIVITY_TYPE_DEFAULT = '0'


def ACTIVITY_TYPE_RETURNER(value):
    if value == '0':
        return 'خالی'
    if value == '1':
        return 'قراردادی'
    if value == '2':
        return 'پیمانی'
    if value == '3':
        return 'رسمی'

    return 'نامعلوم'


FIELD_OF_STUDY_CHOICES = (
    ('0', 'خالی'),
)

FIELD_OF_STUDY_DEFAULT = '0'


def FIELD_OF_STUDY_RETURNER(value):
    if value == '0':
        return 'خالی'
    return 'نامعلوم'
