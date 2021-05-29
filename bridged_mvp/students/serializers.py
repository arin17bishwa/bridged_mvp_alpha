from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import (Student, )


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        email = value
        _ = self
        if email == '' or email is None:
            raise serializers.ValidationError({'email': ['Email field is required']})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists")
        return value

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            is_active=True  # TO BE CHANGED TO FALSE
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'confirm_password': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account
