# Generated by Django 5.0.2 on 2024-10-26 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_ownuserpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownuserpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 26, 12, 26, 43, 796027, tzinfo=datetime.timezone.utc), verbose_name='дата публікації'),
        ),
    ]
