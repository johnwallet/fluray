# Generated by Django 3.1 on 2021-01-18 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0015_auto_20210110_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticdailyprofit',
            options={'verbose_name': 'Статистику прибыли', 'verbose_name_plural': 'Статистика прибыли'},
        ),
        migrations.AlterModelOptions(
            name='transfer',
            options={'verbose_name': 'Внутренний перевод', 'verbose_name_plural': 'Внутренний перевод'},
        ),
    ]