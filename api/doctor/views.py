from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from api.doctor.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = DoctorSerializer


