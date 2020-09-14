# Generated by Django 3.1 on 2020-09-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0011_requestchange_typechange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestchange',
            name='request_type',
        ),
        migrations.AlterField(
            model_name='requestchange',
            name='request_status',
            field=models.CharField(default='в обработке', max_length=150, verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='requestchange',
            name='request_user',
            field=models.CharField(max_length=150, verbose_name='Логин пользователя'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(default='выполнена', max_length=150, verbose_name='Статус'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='TypeChange',
        ),
    ]