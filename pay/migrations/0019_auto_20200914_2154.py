# Generated by Django 3.1 on 2020-09-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0018_auto_20200913_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestchange',
            name='request_status',
            field=models.CharField(default='В обработке', max_length=150, verbose_name='Статус заявки'),
        ),
    ]
