# Generated by Django 5.0.2 on 2024-10-27 18:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_ownuserpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownuserpost',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата публікації'),
        ),
    ]