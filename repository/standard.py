import re


def standard_phone_number(phone_number: str):
    if re.compile(r'^9[0-9]{9}$').match(phone_number) is not None:
        return f'0{phone_number}'
    if re.compile(r'^09[0-9]{9}$').match(phone_number) is not None:
        return phone_number
    if re.compile(r'^\+989[0-9]{9}$').match(phone_number) is not None:
        phone_number = phone_number[3:-1]
        return f'0{phone_number}'
    return None


def standard_gender(gender: str) -> str:
    if gender == '' or \
            gender == 'blank' or \
            gender == 'خالی':
        return '0'

    if gender == 'famale' or \
            gender == 'women' or \
            gender == 'زن' or \
            gender == 'خانوم':
        return '1'
    if gender == 'male' or \
            gender == 'men' or \
            gender == 'مرد' or \
            gender == 'آقا':
        return '2'

    return '3'


def standard_birth_date(birth_date: str, btype: str = 'solar'):
    birth_date = birth_date.split('-')
    if len(birth_date) != 3:
        return None
    import jdatetime
    import datetime
    year = int(birth_date[0])
    month = int(birth_date[1])
    day = int(birth_date[2])
    now = jdatetime.date.today()
    if btype == 'solar':
        now = jdatetime.date.today()

    if btype == 'gregorian':
        now = datetime.date.today()

    birth_date = datetime.date(year=year, month=month, day=day)
    if birth_date > now:
        return None
    return birth_date


def standard_birth_place(birth_place_id: str):
    from base_information_settings.models import Zone
    return Zone.objects.filter(code=birth_place_id).first()


def standard_zone(zone_id: str):
    from base_information_settings.models import Zone
    return Zone.objects.filter(code=zone_id).first()


def standard_official_website(official_website: str):
    return None


def standard_avatar(avatar: str):
    return None


def standard_nationality(nationality_id: str):
    from base_information_settings.models import BaseInformation
    return BaseInformation.objects.filter(pk=nationality_id).first()


def standard_religion(religion_id: str):
    from base_information_settings.models import BaseInformation
    return BaseInformation.objects.filter(pk=religion_id).first()


def standard_base_information_obj(obj_id: str):
    from base_information_settings.models import BaseInformation
    return BaseInformation.objects.filter(pk=obj_id).first()


def standard_date(date: str):
    date = date.split('-')
    if len(date) != 3:
        return None
    import datetime
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    date = datetime.date(year=year, month=month, day=day)
    return date


def standard_url(url: str):
    return None


def standard_file(file: str):
    return None


def standard_user(user_id: str):
    from users.models import User
    return User.objects.filter(pk=user_id).first()
