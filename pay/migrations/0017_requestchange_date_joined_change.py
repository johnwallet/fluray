# Generated by Django 3.1 on 2020-09-13 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0016_auto_20200913_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestchange',
            name='date_joined_change',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Заявка создана'),
        ),
    ]