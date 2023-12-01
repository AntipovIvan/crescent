from django.contrib import admin
from django import forms
from .models import *


class YourModelAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ContentInline(admin.StackedInline):
    model = Content


class ImageInline(admin.StackedInline):
    model = Image


class YourModelAdmin(admin.ModelAdmin):
    form = YourModelAdminForm
    inlines = [ContentInline, ImageInline]
    list_display = ["title", "sorting_order"]  # Display fields in the list view

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "sorting_order":
            kwargs["widget"] = forms.NumberInput(
                attrs={"style": "width: 50px"}
            )  # Customize widget style
        return super().formfield_for_dbfield(db_field, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by(
            "sorting_order"
        )  # Sorting by the sorting_order field
        return queryset


admin.site.register(Product, YourModelAdmin)
admin.site.register(NewsModel)
admin.site.register(ServicesModel)
