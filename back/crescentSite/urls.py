from crescentSite import views
from django.urls import include, path
from rest_framework import routers
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"newsmodels", views.NewsModelViewSet)
router.register(r"usercase", views.UsercaseViewSet)
router.register(r"special", views.SpecialViewSet)
router.register(r"blog", views.BlogViewSet)
router.register(r"product", views.ProductViewSet)
router.register(r"servicesmodels", views.ServicesModelViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
