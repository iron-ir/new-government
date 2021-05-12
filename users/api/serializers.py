from rest_framework import serializers
from users.models import User


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
