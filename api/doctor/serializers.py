from django.contrib.auth.models import User, Group
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'