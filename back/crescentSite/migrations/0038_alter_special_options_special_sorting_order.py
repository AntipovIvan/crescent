# Generated by Django 4.2.3 on 2023-12-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crescentSite', '0037_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='special',
            options={'ordering': ['sorting_order'], 'verbose_name_plural': 'Special Feature'},
        ),
        migrations.AddField(
            model_name='special',
            name='sorting_order',
            field=models.IntegerField(default=0),
        ),
    ]
