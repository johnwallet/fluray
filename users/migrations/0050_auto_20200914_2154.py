# Generated by Django 3.1 on 2020-09-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_remove_customuser_balancebtc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='balance',
        ),
        migrations.AddField(
            model_name='customuser',
            name='balanceeur',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Баланс EUR'),
        ),
    ]
