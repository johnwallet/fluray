# Generated by Django 3.1 on 2021-01-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0004_auto_20210107_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestchange',
            name='date_end_change',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата исполнения'),
        ),
    ]