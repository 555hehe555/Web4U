# Generated by Django 5.0.2 on 2024-02-22 15:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/%Y', verbose_name='зображеня'),
            preserve_default=False,
        ),
    ]