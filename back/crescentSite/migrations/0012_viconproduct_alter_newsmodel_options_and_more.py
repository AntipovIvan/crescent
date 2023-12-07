# Generated by Django 4.2.3 on 2023-11-27 09:46

import crescentSite.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("crescentSite", "0011_newsmodel_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="ViconProduct",
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
                ("title", models.CharField(max_length=100)),
                ("contents", models.TextField(blank=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("CAMERA", "CAMERA"),
                            ("SOFTWARE", "SOFTWARE"),
                            ("HARDWARE", "HARDWARE"),
                        ],
                        default="モーションキャプチャー",
                        max_length=20,
                    ),
                ),
                ("images", models.ImageField(default="images/Placeholder.png")),
            ],
            options={
                "verbose_name_plural": "Vicon products",
            },
        ),
        migrations.AlterModelOptions(
            name="newsmodel",
            options={"verbose_name_plural": "News"},
        ),
        migrations.AlterModelOptions(
            name="productcardmodel",
            options={"verbose_name_plural": "Product cards"},
        ),
        migrations.AlterModelOptions(
            name="servicesmodel",
            options={"verbose_name_plural": "Services"},
        ),
        migrations.AlterField(
            model_name="productcardmodel",
            name="category",
            field=models.CharField(
                choices=[
                    ("モーションキャプチャー", "MOTION_CAPTURE"),
                    ("ボリュメトリックキャプチャー", "VOLUMETRICS_CAPTURE"),
                    ("フォトグラフメトリ", "PHOTOGRAMMETRY"),
                    ("Coming soon", "COMING_SOON"),
                ],
                default="CAMERA",
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Image",
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
                ("title", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(
                        upload_to=crescentSite.models.Image.upload_to
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crescentSite.viconproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Content",
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
                ("content", models.TextField(blank=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crescentSite.viconproduct",
                    ),
                ),
            ],
        ),
    ]