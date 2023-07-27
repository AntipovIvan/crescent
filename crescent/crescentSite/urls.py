from django.urls import path
from crescentSite import views

urlpatterns = [
    path("", views.index, name="index"),
]
