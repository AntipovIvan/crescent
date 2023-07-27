from django.urls import path
from crescent import views

urlpatterns = [
    path("", views.index, name="index"),
]
