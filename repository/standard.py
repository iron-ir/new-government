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


def standard_birth_date(birth_date: str):
    return None


def standard_birth_place(birth_place_code: str):
    birth_place_code = int(birth_place_code)
    from base_information_setting.models import Zone
    return Zone.objects.filter(code=birth_place_code).first()


def standard_official_website(official_website: str):
    return None


def standard_avatar(avatar: str):
    return None
