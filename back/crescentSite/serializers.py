from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class ProductContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = "__all__"


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
            "category",
            "created_at",
            "updated_at",
        ]


class UsercaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usercase
        fields = [
            "id",
            "date",
            "title",
            "thumbnail",
            "content",
            "created_at",
            "updated_at",
        ]


class SpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Special
        fields = [
            "id",
            "date",
            "title",
            "thumbnail",
            "content",
            "created_at",
            "updated_at",
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    productContent = ProductContentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "category",
            "description",
            "hero",
            "productContent",
            "thumbnail",
            "sorting_order",
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
