from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib import admin
from ckeditor.fields import RichTextField
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
    ("EVENT", "イベント"),
    ("PRODUCT_INFO", "製品情報"),
    ("NOTICE", "お知らせ"),
)

PRODUCT_SECTIONS = (
    ("OVERVIEW", "概要"),
    ("USAGE", "用途"),
    ("DETAILS_PRICE", "詳細・金額"),
    ("CATALOG_DOWNLOAD", "カタログダウンロード"),
    ("OTHER", "その他"),
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

    def upload_to(self, filename):
        date = self.date if self.date else "default"
        date = str(date)
        return os.path.join("images/news", date, filename)

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
    description = models.CharField(max_length=50, blank=True)
    sorting_order = models.IntegerField(default=0)

    def upload_to(self, filename):
        title = self.title if self.title else "default"
        title = title.replace(" ", "_")
        return os.path.join("images", title, filename)

    thumbnail = models.ImageField(
        upload_to=upload_to, default="images/Placeholder.png"
    )
    hero = models.ImageField(
        upload_to=upload_to, default="images/Placeholder.png"
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Product"
        ordering = ["sorting_order"]


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


class ProductContent(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="productContent"
    )

    def upload_to(self, filename):
        return self.product.upload_to(filename)

    section = models.CharField(
        max_length=20, choices=PRODUCT_SECTIONS, default="概要"
    )

    productTitle = models.CharField(
        max_length=100, verbose_name="Title", blank=True
    )
    image = models.ImageField(
        upload_to=upload_to, verbose_name="Image", blank=True
    )
    productText = RichTextField(verbose_name="Text")

    def __str__(self):
        return f"{self.productTitle}"

    class Meta:
        verbose_name_plural = "Product Content"


class NewsImages(models.Model):
    product = models.ForeignKey(
        NewsModel, on_delete=models.CASCADE, related_name="images"
    )

    def upload_to(self, filename):
        return self.product.upload_to(filename)

    image = models.ImageField(upload_to=upload_to)


@receiver(pre_delete, sender=Image)
@receiver(pre_delete, sender=ProductContent)
@receiver(pre_delete, sender=NewsImages)
def delete_image_files(sender, instance, **kwargs):
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
