from repository.regular_expression import *
from repository.manage_data_rules import Rules


# to rules -> [moods] and on mood -> {objects} and on objects -> {fields} and fields -> {features}

def login_rules_input() -> list:
    return [
        {
            'user': {
                'username': {},
                'password': {},
            },
        },
        {
            'user': {
                'phone_number': {},
                'password': {},
            },
        },
        {
            'user': {
                'email': {},
                'password': {},
            },
        },
        {
            'user': {
                'national_code': {},
                'password': {},
            },
        },
    ]


def login_rules_output() -> list:
    return [
        {
            'user': {
                '__all__': {},
            },
            'user_role': {
                'id': {},
                'from_date_time': {},
                'to_date_time': {},
                'role_id': {},
            },
            'work_expiration': {
                'id': {},
                'place_number_for_sorting': {},
                'is_verify': {},
                'post_title': {},
                'cooperation_type_id': {},
                'from_date': {},
                'to_date': {},
                'activity_type_id': {},
                'organization_name': {},
            },
            'education_history': {
                'id': {},
                'place_number_for_sorting': {},
                'is_verify': {},
                'degree_type_id': {},
                'field_of_study_id': {},
                'place_of_study_type_id': {},
                'place_of_study': {},
                'zone_id': {},
                'graduation_date': {},
                'is_study': {},
            },
            'standpoints': {
                'id': {},
                'place_number_for_sorting': {},
                'title': {},
                'description': {},
                'is_active': {},
                'link': {},
                'attachment': {},
            },
            'effects': {
                'id': {},
                'type_id': {},
                'place_number_for_sorting': {},
                'is_active': {},
                'title': {},
                'description': {},
                'link': {},
                'attachment': {},
            },
            'user_relation': {
                'id': {},
                'is_verify': {},
                'base_user_id': {},
                'base_user_verification': {},
                'related_user_id': {},
                'related_user_verification': {},
                'type_id': {},
                'form_date': {},
                'to_date': {},
            },

        },
    ]


LOGIN_RULES = Rules()
LOGIN_RULES.INPUT = login_rules_input()
LOGIN_RULES.OUTPUT = login_rules_output()
