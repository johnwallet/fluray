# Generated by Django 3.1 on 2021-01-07 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0005_auto_20210107_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_end_change',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Исполнена'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_joined_change',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создана'),
        ),
    ]