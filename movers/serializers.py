from .models import *
from rest_framework import serializers, fields




class UserBreaksserializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('__all__')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        if data['email'] == '':
            raise serializers.ValidationError('Email Field Empty')
        if data['password'] == '':
            raise serializers.ValidationError('Password Field Empty')

        return data
