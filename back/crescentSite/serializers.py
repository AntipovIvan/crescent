from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "url", "name"]


class NewsModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsModel
        fields = [
            "id",
            "date",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]


class ProductCardModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCardModel
        fields = [
            "id",
            "title",
            "content",
            "category",
            "thumbnail",
        ]


class ServicesModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServicesModel
        fields = [
            "id",
            "title",
            "content",
            "thumbnail",
        ]
