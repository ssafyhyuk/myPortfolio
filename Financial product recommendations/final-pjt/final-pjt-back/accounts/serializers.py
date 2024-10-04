from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(
        required=True,
    )
    asset = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    income = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    nickname = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    image = serializers.ImageField(required=False, allow_null=True, use_url=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age', 0),
            'asset': self.validated_data.get('asset', ''),
            'income': self.validated_data.get('income', ''),
            'nickname': self.validated_data.get('nickname', ''),

            'image': self.validated_data.get('image', None)
        }
    
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')

        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'asset'):
            extra_fields.append('asset')    
        if hasattr(UserModel, 'income'):
            extra_fields.append('income')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')

        if hasattr(UserModel, 'image'):
            extra_fields.append('image')

        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'