from .models import *
from rest_framework import serializers, fields




class UserBreaksserializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('__all__')