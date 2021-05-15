from repository.regular_expression import (
    username_reg,
    email_reg,
    password_reg,
    phonenumber_reg,
    postalcode_reg,
    nationalcode_reg,
    time_reg,
    date_reg,
    date_time_reg,
    string_reg,
    integer_reg,
    float_reg,
    text_teg,
)

OBJECTS_LIST = {
    'user': {
        'id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'password': {
            'null_able': False,
            'validator': password_reg,
            'max_length': None,
            'min_length': None,
        },
        'is_verify': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
        'is_email_verify': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
        'is_phone_number_verify': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
        'is_personal_information_verify': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
        'username': {
            'null_able': False,
            'validator': username_reg,
            'max_length': None,
            'min_length': None,
        },
        'email': {
            'null_able': False,
            'validator': email_reg,
            'max_length': None,
            'min_length': None,
        },
        'phone_number': {
            'null_able': False,
            'validator': phonenumber_reg,
            'max_length': None,
            'min_length': None,
        },
        'avatar_path': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
        'first_name': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'last_name': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'gender': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'national_code': {
            'null_able': False,
            'validator': nationalcode_reg,
            'max_length': None,
            'min_length': None,

        },
        'father_name': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'mother_name': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'birth_date': {
            'null_able': False,
            'validator': date_reg,
            'max_length': None,
            'min_length': None,

        },
        'birth_place_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'nationality_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'religion_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'official_website': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,

        },
        'last_login': {
            'null_able': False,
            'validator': date_time_reg,
            'max_length': None,
            'min_length': None,

        },
    },
    'register_candidate_per_election': {
        'id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'candidate_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'elections_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'candidate_group_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'date_time': {
            'null_able': False,
            'validator': date_time_reg,
            'max_length': None,
            'min_length': None,
        },
        'slogan': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'candidate_title': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'place_id': {
            'null_able': False,
            'validator': None,
            'max_length': None,
            'min_length': None,
        },
    },
    'user_role': {
        'from_date_time': {
            'null_able': False,
            'validator': date_time_reg,
            'max_length': None,
            'min_length': None,
        },
        'to_date_time': {
            'null_able': False,
            'validator': date_time_reg,
            'max_length': None,
            'min_length': None,
        },
        'user_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
        'role_id': {
            'null_able': False,
            'validator': string_reg,
            'max_length': None,
            'min_length': None,
        },
    },
}


class Rules:
    INPUT: list
    OUTPUT: list


def is_object(obj_name: str):
    if obj_name in OBJECTS_LIST.keys():
        return True
    return False


def is_field_belongs_object(obj_name: str, field_name: str):
    if not is_object(obj_name):
        return None

    obj = OBJECTS_LIST[obj_name]
    if field_name in obj.keys():
        return True

    return False


def is_condition_met(obj_name, field_name, value, attr_name, attr_value=None):
    if is_field_belongs_object(obj_name, field_name) is None:
        return None

    obj = OBJECTS_LIST[obj_name]
    field = obj[field_name]

    if attr_name == 'null_able':
        if attr_value is None:
            attr_value = field[attr_name]
        if attr_value is True:
            return True
        if value is not None:
            if len(value) != 0:
                return True
        return False

    if attr_name == 'validator':
        if attr_value is None:
            attr_value = field[attr_name]
        if attr_value is None:
            return True
        if value is None:
            return False
        if attr_value.match(value) is None:
            return False
        return True

    if attr_name == 'max_length':
        if attr_value is None:
            attr_value = field[attr_name]
        if attr_value is None:
            return True
        if len(value) <= attr_value:
            return True
        return False

    if attr_name == 'min_length':
        if attr_value is None:
            attr_value = field[attr_name]
        if attr_value is None:
            return True
        if len(value) >= attr_value:
            return True
        return False


def clean_values(rules, values_list):
    c_value = []
    for rule in rules:
        _objs = {}
        for obj_name, obj_value in rule.items():
            _fields = {}
            for field_name, field_value in obj_value.items():
                r_field_name = f'{obj_name}.{field_name}'
                if r_field_name in values_list:
                    _fields[field_name] = values_list[r_field_name]
                else:
                    _fields[field_name] = None
            _objs[obj_name] = _fields
        c_value.append(_objs)
    return c_value


def set_default(rules):
    default_rules = []
    for rule in rules:
        objs = {}
        for obj_name, obj_value in rule.items():
            fields = {}
            for field_name, field_value in obj_value.items():
                attr_default = OBJECTS_LIST[obj_name][field_name]
                attrs = {}
                for attr_default_name, attr_default_value in attr_default.items():
                    if attr_default_name in field_value:
                        attrs[attr_default_name] = field_value[attr_default_name]
                    else:
                        attrs[attr_default_name] = attr_default_value
                fields[field_name] = attrs
            objs[obj_name] = fields
        default_rules.append(objs)
    return default_rules


def law_enforcement_manager(rules: list, values_list: list):
    values_list = clean_values(rules, values_list)
    rules = set_default(rules)
    err_list = []
    err_flag = False
    for i in range(len(rules)):
        err_flag = False
        rule = rules[i]
        for obj_name, obj_value in rule.items():
            if err_flag:
                break
            for field_name, field_value in obj_value.items():
                if err_flag:
                    break
                value = values_list[i][obj_name][field_name]
                for attr_name, attr_value in field_value.items():
                    if err_flag:
                        break
                    if not is_condition_met(obj_name, field_name, value, attr_name, attr_value):
                        err_flag = True
                        err_list.append(
                            f'{obj_name}_{field_name} :: attribute name: {attr_name}, attribute value: {attr_value}'
                        )
        if not err_flag:
            values_list = values_list[i]
            break
    if err_flag:
        # todo error handling
        raise Exception('input fields error')
    return values_list
