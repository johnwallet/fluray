# Generated by Django 3.1 on 2021-01-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210108_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='reserv_vtb_rub',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='ВТБ'),
        ),
    ]