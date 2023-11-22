from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *


def index(request):
    return render(request, "index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductCardModelViewSet(viewsets.ModelViewSet):
    queryset = ProductCardModel.objects.all()
    serializer_class = ProductCardModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ServicesModelViewSet(viewsets.ModelViewSet):
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesModelSerializer
    # permission_classes = [permissions.IsAuthenticated]