# Generated by Django 3.1 on 2021-02-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210210_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='line_program',
            name='line_ref_link',
            field=models.CharField(default=0, max_length=50, verbose_name='Реферальная ссылка'),
            preserve_default=False,
        ),
    ]
