# Generated by Django 4.2.3 on 2023-12-08 00:12

import crescentSite.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("crescentSite", "0018_alter_newsmodel_category_newsimages"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testcontent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("testtitle", models.CharField(max_length=100)),
                (
                    "testimage",
                    models.ImageField(
                        upload_to=crescentSite.models.ProductContent.upload_to
                    ),
                ),
                ("testcontent", models.TextField(blank=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testcontent",
                        to="crescentSite.product",
                    ),
                ),
            ],
        ),
    ]
