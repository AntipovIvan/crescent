from django.contrib import admin
from django import forms
from .models import *
from adminsortable2.admin import SortableAdminMixin


class ProductContentInline(admin.StackedInline):
    model = ProductContent
    extra = 0


class NewsImagesInline(admin.StackedInline):
    model = NewsImages


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = "__all__"


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductContentInline]
    list_display = [
        "title",
        "sorting_order",
        "category",
    ]  # Display fields in the list view


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    inlines = [NewsImagesInline]
    list_display = [
        "date",
        "title",
        "category",
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(ServicesModel)
