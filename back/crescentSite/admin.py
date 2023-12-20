from django.contrib import admin
from django import forms
from .models import *
from adminsortable2.admin import SortableAdminMixin


class ProductContentInline(admin.StackedInline):
    model = ProductContent
    extra = 0


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = "__all__"


class UsercaseAdminForm(forms.ModelForm):
    class Meta:
        model = Usercase
        fields = "__all__"


class SpecialAdminForm(forms.ModelForm):
    class Meta:
        model = Special
        fields = "__all__"


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
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
    list_display = [
        "date",
        "title",
        "category",
    ]


class UsercaseAdmin(admin.ModelAdmin):
    form = UsercaseAdminForm
    list_display = [
        "date",
        "title",
    ]


class SpecialAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = SpecialAdminForm
    list_display = [
        "date",
        "title",
        "sorting_order",
    ]


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = [
        "date",
        "title",
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(Usercase, UsercaseAdmin)
admin.site.register(Special, SpecialAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(ServicesModel)
