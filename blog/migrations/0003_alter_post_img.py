# Generated by Django 5.0.2 on 2024-02-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='image/%Y', verbose_name='зображеня'),
        ),
    ]