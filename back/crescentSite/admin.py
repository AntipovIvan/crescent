from django.contrib import admin
from .models import *


class ContentInline(admin.StackedInline):
    model = Content


class ImageInline(admin.StackedInline):
    model = Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ContentInline, ImageInline]


admin.site.register(NewsModel)
admin.site.register(ServicesModel)
