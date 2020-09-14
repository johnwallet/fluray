# Generated by Django 3.1 on 2020-09-13 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0017_requestchange_date_joined_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestchange',
            name='request_userchange',
            field=models.CharField(blank=True, max_length=150, verbose_name='Обработчик заявки'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_joined_change',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Заявка создана'),
        ),
        migrations.AlterField(
            model_name='requestchange',
            name='date_joined_change',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]