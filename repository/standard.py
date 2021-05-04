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
