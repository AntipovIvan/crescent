from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
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
    images = NewsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = NewsModel
        fields = [
            "id",
            "date",
            "title",
            "content",
            "images",
            "category",
            "created_at",
            "updated_at",
        ]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "contents",
            "category",
            "images",
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
