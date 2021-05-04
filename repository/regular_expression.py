import re
from django.core import validators
from django.utils.deconstruct import deconstructible

_username_regular_expression = r'^[A-Za-z0-9!@#$&*_.]{3,20}$'
_password_regular_expression = r'^[A-Za-z0-9!@#$&*_.]{8,20}$'
_phonenumber_regular_expression = r'^(|0|\+98)9[0-9]{9}$'
_nationalcode_regular_expression = r'^[0-9]{10}$'
_postalcode_regular_expression = r'^[0-9]{10}$'
_email_regular_expression = r"^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$"

username_reg = re.compile(_username_regular_expression)
password_reg = re.compile(_password_regular_expression)
phonenumber_reg = re.compile(_phonenumber_regular_expression)
nationalcode_reg = re.compile(_nationalcode_regular_expression)
postalcode_reg = re.compile(_postalcode_regular_expression)
email_reg = re.compile(_email_regular_expression)


@deconstructible
class UnicodePasswordValidator(validators.RegexValidator):
    regex = _password_regular_expression
    message = "The password is only allowed in combination of eight to twenty characters from" \
              " the following characters.\n- All lowercase English letters\n- All English uppercase" \
              " letters\n- All English numbers\n- Characters! @ # $ & * _."
    flags = 0


@deconstructible
class UnicodePhoneNumberValidator(validators.RegexValidator):
    regex = _phonenumber_regular_expression
    message = 'Enter a valid phonenumber.'
    flags = 0


@deconstructible
class UnicodeNationalcodeValidator(validators.RegexValidator):
    regex = _nationalcode_regular_expression
    message = 'Enter a valid nationalcode.'
    flags = 0
