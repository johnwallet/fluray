# Generated by Django 3.1 on 2021-02-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20210212_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_program',
            name='fio_ref',
            field=models.CharField(default='', max_length=250, verbose_name='ФИО'),
        ),
    ]