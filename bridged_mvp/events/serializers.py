from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import (Event, )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
