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

class MoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mover
        fields = ('__all__')

class SignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    gender= serializers.CharField(max_length=255)
    dob = serializers.DateField()

class UsersignupSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class RequestMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('__all__')

