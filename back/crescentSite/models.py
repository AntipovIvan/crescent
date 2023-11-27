from django.db import models
from django.contrib import admin
import os

# Specifying the choices
PRODUCTS_CATEGORIES = (
    ("モーションキャプチャー", "MOTION_CAPTURE"),
    ("ボリュメトリックキャプチャー", "VOLUMETRICS_CAPTURE"),
    ("フォトグラフメトリ", "PHOTOGRAMMETRY"),
    ("Coming soon", "COMING_SOON"),
)

NEWS_CATEGORIES = (
    ("イベント", "EVENT"),
    ("製品情報", "PRODUCT_INFO"),
    ("その他", "OTHER"),
)

VICON_PRODUCTS_CATEGORIES = (
    ("CAMERA", "CAMERA"),
    ("SOFTWARE", "SOFTWARE"),
    ("HARDWARE", "HARDWARE"),
)


class NewsModel(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    category = models.CharField(
        max_length=20, choices=NEWS_CATEGORIES, default="イベント"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"


class ProductCardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    category = models.CharField(
        max_length=20, choices=PRODUCTS_CATEGORIES, default="CAMERA"
    )

    def upload_to(self, filename):
        title = self.title if self.title else "default"
        title = title.replace(" ", "_")
        return os.path.join("images", title, filename)

    thumbnail = models.ImageField(
        upload_to=upload_to, default="images/Placeholder.png"
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product cards"


class ViconProduct(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    category = models.CharField(
        max_length=20, choices=VICON_PRODUCTS_CATEGORIES, default="モーションキャプチャー"
    )

    def upload_to(self, filename):
        title = self.title if self.title else "default"
        title = title.replace(" ", "_")
        return os.path.join("images", title, filename)

    images = models.ImageField(
        upload_to=upload_to, default="images/Placeholder.png"
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Vicon products"


# Nested models for content and images
class Content(models.Model):
    product = models.ForeignKey(ViconProduct, on_delete=models.CASCADE)
    content = models.TextField(blank=True)


class Image(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(ViconProduct, on_delete=models.CASCADE)

    def upload_to(self, filename):
        title = self.title if self.title else "default"
        title = title.replace(" ", "_")
        return os.path.join("images", title, filename)

    image = models.ImageField(upload_to=upload_to)


class ServicesModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def upload_to(self, filename):
        title = self.title if self.title else "default"
        title = title.replace(" ", "_")
        return os.path.join("images", title, filename)

    thumbnail = models.ImageField(
        upload_to=upload_to, default="images/Placeholder.png"
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"
