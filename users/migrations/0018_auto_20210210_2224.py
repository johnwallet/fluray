# Generated by Django 3.1 on 2021-02-10 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210210_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line_program',
            old_name='line_parent',
            new_name='parent',
        ),
    ]