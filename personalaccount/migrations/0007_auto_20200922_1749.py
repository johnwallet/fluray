# Generated by Django 3.1 on 2020-09-22 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0006_auto_20200922_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestchange',
            name='criteri',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.criterichange', verbose_name='Критерий'),
        ),
    ]