# Generated by Django 5.0.2 on 2024-09-20 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_ownuserpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownuserpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 20, 18, 15, 52, 89386, tzinfo=datetime.timezone.utc), verbose_name='дата публікації'),
        ),
        migrations.AlterField(
            model_name='ownuserpost',
            name='img',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='зображеня'),
        ),
    ]
