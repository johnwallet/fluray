# Generated by Django 3.1 on 2020-09-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestchange',
            name='request_type',
            field=models.CharField(default='Заявка на пополнение', max_length=150, verbose_name='Тип заявки'),
        ),
    ]