from rest_framework import serializers
from users.models import User
from repository.db_manager import paginate


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'phone_number',
            'is_phone_number_verify',
            'email',
            'is_email_verify',
            'avatar',
        ]


def user_list_serializer(users: User, page: int, page_size: int):
    users = paginate(users, page, page_size)
    _users = []
    for user in users:
        _users.append(
            {
                'id': user.pk,
                'is_verify': user.is_verify,
                'avatar': str(user.avatar),
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        )

    return _users


def user_serializer(user: User):
    pass

    # _roles = user.userrole_set.all()
    # for role in _roles:
    #
    #
    # return {
    #     'id': user.pk,
    #     'is_verify': user.is_verify,
    #     'is_email_verify': user.is_email_verify,
    #     'is_phone_number_verify': user.is_phone_number_verify,
    #     'is_personal_information_verify': user.is_personal_information_verify,
    #     'username': user.username,
    #     'email': user.email,
    #     'phone_number': user.phone_number,
    #     'avatar': str(user.avatar),
    #     'first_name': user.first_name,
    #     'last_name': user.last_name,
    #     'gender': user.gender,
    #     'national_code': user.national_code,
    #     'father_name': user.father_name,
    #     'mother_name': user.mother_name,
    #     'birth_date': user.birth_date,
    #     'birth_place': user.birth_place,
    #     'nationality': user.nationality,
    #     'religion': user.religion,
    #     'official_website': str(user.official_website),
    #     'last_login': user.last_login,
    #
    #     'role':
    # }
