from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib import admin
import os

# Specifying the choices
PRODUCTS_CATEGORIES = (
    ("MOTION_CAPTURE", "モーションキャプチャー"),
    ("VOLUMETRICS_CAPTURE", "ボリュメトリックキャプチャー"),
    ("PHOTOGRAMMETRY", "フォトグラフメトリ"),
    ("CAMERA", "CAMERA"),
    ("SOFTWARE", "SOFTWARE"),
    ("HARDWARE", "HARDWARE"),
    ("COMING_SOON", "Coming soon"),
)

NEWS_CATEGORIES = (
    ("イベント", "EVENT"),
    ("製品情報", "PRODUCT_INFO"),
    ("その他", "OTHER"),
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


class Product(models.Model):
    title = models.CharField(max_length=100)
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
        verbose_name_plural = "Product"


# Nested models for content and images
class Content(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="contents"
    )
    content = models.TextField(blank=True)


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    def upload_to(self, filename):
        return self.product.upload_to(filename)

    image = models.ImageField(upload_to=upload_to)


@receiver(pre_delete, sender=Image)
def delete_image_files(sender, instance, **kwargs):
    # Delete the physical file when an Image object is deleted
    instance.image.delete(save=False)


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
