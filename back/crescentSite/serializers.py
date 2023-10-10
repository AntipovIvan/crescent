from django.contrib.auth.models import User, Group
from .models import YourModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "url", "name"]


class YourModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YourModel
        fields = ["id", "field1", "field2", "additional_field2", "cover"]
