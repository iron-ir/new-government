import re
from django.core import validators
from django.utils.deconstruct import deconstructible

_username_regular_expression = r'^.{3,20}$'
_password_regular_expression = r'^.{8,20}$'
_phonenumber_regular_expression = r'^(|0|\+98)9[0-9]{9}$'
_nationalcode_regular_expression = r'^[0-9]{10}$'
_postalcode_regular_expression = r'^[0-9]{10}$'

username_reg = re.compile(_username_regular_expression)
password_reg = re.compile(_password_regular_expression)
phonenumber_reg = re.compile(_phonenumber_regular_expression)
nationalcode_reg = re.compile(_nationalcode_regular_expression)
postalcode_reg = re.compile(_postalcode_regular_expression)


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

