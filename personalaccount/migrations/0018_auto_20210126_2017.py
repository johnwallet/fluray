# Generated by Django 3.1 on 2021-01-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0017_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_instagram',
            field=models.URLField(default='https://www.instagram.com/', verbose_name='Пост в инстаграме'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_telegram',
            field=models.URLField(default='https://telegram.org/', verbose_name='Пост в инстаграме'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_content',
            field=models.TextField(max_length=500, verbose_name='Контент'),
        ),
    ]