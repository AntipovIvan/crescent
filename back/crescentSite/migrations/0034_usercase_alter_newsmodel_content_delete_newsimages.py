# Generated by Django 4.2.3 on 2023-12-14 09:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crescentSite', '0033_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usercase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('title', models.CharField(max_length=150)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text')),
                ('sorting_order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Usercase',
                'ordering': ['sorting_order'],
            },
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text'),
        ),
        migrations.DeleteModel(
            name='NewsImages',
        ),
    ]
