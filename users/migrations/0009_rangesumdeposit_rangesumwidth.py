# Generated by Django 3.1 on 2021-01-31 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210130_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeSumWidth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width_min_sberbank_rub', models.IntegerField(verbose_name='СБЕРБАНК')),
                ('width_min_psb_rub', models.IntegerField(verbose_name='ПСБ')),
                ('width_min_tinkoff_rub', models.IntegerField(verbose_name='ТИНЬКОФФ')),
                ('width_min_gazprombank_rub', models.IntegerField(verbose_name='ГАЗПРОМБАНК')),
                ('width_min_alfabank_rub', models.IntegerField(verbose_name='АЛЬФАБАНК')),
                ('width_min_russtandart_rub', models.IntegerField(verbose_name='РУССКИЙСТАНДАРТ')),
                ('width_min_vtb_rub', models.IntegerField(verbose_name='ВТБ')),
                ('width_min_rosselhoz_rub', models.IntegerField(verbose_name='РОССЕЛЬХОЗБАНК')),
                ('width_min_raifaizen_rub', models.IntegerField(verbose_name='РАЙФАЙЗЕНБАНК')),
                ('width_min_otkritie_rub', models.IntegerField(verbose_name='ОТКРЫТИЕ')),
                ('width_min_pochtabank_rub', models.IntegerField(verbose_name='ПОЧТАБАНК')),
                ('width_min_rnkb_rub', models.IntegerField(verbose_name='РНКБ')),
                ('width_min_rosbank_rub', models.IntegerField(verbose_name='РОСБАНК')),
                ('width_min_mtsbank_rub', models.IntegerField(verbose_name='МТСБАНК')),
                ('width_min_qiwi_rub', models.IntegerField(verbose_name='КИВИРУБ')),
                ('width_min_qiwi_usd', models.IntegerField(verbose_name='КИВИДОЛЛАР')),
                ('width_min_payeer_rub', models.IntegerField(verbose_name='ПАЕЕРРУБ')),
                ('width_min_payeer_usd', models.IntegerField(verbose_name='ПАЕЕРДОЛЛАР')),
                ('width_min_payeer_eur', models.IntegerField(verbose_name='ПАЕЕРЕВРО')),
                ('width_min_webmoney_rub', models.IntegerField(verbose_name='ВЕБМАНИРУБ')),
                ('width_min_webmoney_usd', models.IntegerField(verbose_name='ВЕБМАНИДОЛЛАР')),
                ('width_min_webmoney_eur', models.IntegerField(verbose_name='ВЕБМАНИЕВРО')),
                ('width_min_pm_btc', models.IntegerField(verbose_name='ПМБИТКОИН')),
                ('width_min_pm_usd', models.IntegerField(verbose_name='ПМДОЛЛАР')),
                ('width_min_pm_eur', models.IntegerField(verbose_name='ПМЕВРО')),
                ('width_min_skrill_eur', models.IntegerField(verbose_name='СКРИЛЛЕВРО')),
                ('width_min_skrill_usd', models.IntegerField(verbose_name='СКРИЛДОЛЛАР')),
                ('width_min_paypal_rub', models.IntegerField(verbose_name='ПАЙПАЛРУБ')),
                ('width_min_paypal_usd', models.IntegerField(verbose_name='ПАЙПАЛДОЛЛАР')),
                ('width_min_paypal_eur', models.IntegerField(verbose_name='ПАЙПАЛЕВРО')),
                ('width_min_umoney_rub', models.IntegerField(verbose_name='ЮМАНИ')),
                ('width_min_btc', models.IntegerField(verbose_name='БИТКОИН')),
                ('width_min_xrp', models.IntegerField(verbose_name='РИПЛ')),
                ('width_min_ltc', models.IntegerField(verbose_name='ЛАЙТКОИН')),
                ('width_min_bch', models.IntegerField(verbose_name='БИТКОИНКЕШ')),
                ('width_min_xmr', models.IntegerField(verbose_name='МОНЕРО')),
                ('width_min_eth', models.IntegerField(verbose_name='ЭФИР')),
                ('width_min_etc', models.IntegerField(verbose_name='ЭФИРКЛАССИК')),
                ('width_min_dash', models.IntegerField(verbose_name='ДАШ')),
                ('width_max_sberbank_rub', models.IntegerField(verbose_name='СБЕРБАНК')),
                ('width_max_psb_rub', models.IntegerField(verbose_name='ПСБ')),
                ('width_max_tinkoff_rub', models.IntegerField(verbose_name='ТИНЬКОФФ')),
                ('width_max_gazprombank_rub', models.IntegerField(verbose_name='ГАЗПРОМБАНК')),
                ('width_max_alfabank_rub', models.IntegerField(verbose_name='АЛЬФАБАНК')),
                ('width_max_russtandart_rub', models.IntegerField(verbose_name='РУССКИЙСТАНДАРТ')),
                ('width_max_vtb_rub', models.IntegerField(verbose_name='ВТБ')),
                ('width_max_rosselhoz_rub', models.IntegerField(verbose_name='РОССЕЛЬХОЗБАНК')),
                ('width_max_raifaizen_rub', models.IntegerField(verbose_name='РАЙФАЙЗЕНБАНК')),
                ('width_max_otkritie_rub', models.IntegerField(verbose_name='ОТКРЫТИЕ')),
                ('width_max_pochtabank_rub', models.IntegerField(verbose_name='ПОЧТАБАНК')),
                ('width_max_rnkb_rub', models.IntegerField(verbose_name='РНКБ')),
                ('width_max_rosbank_rub', models.IntegerField(verbose_name='РОСБАНК')),
                ('width_max_mtsbank_rub', models.IntegerField(verbose_name='МТСБАНК')),
                ('width_max_qiwi_rub', models.IntegerField(verbose_name='КИВИРУБ')),
                ('width_max_qiwi_usd', models.IntegerField(verbose_name='КИВИДОЛЛАР')),
                ('width_max_payeer_rub', models.IntegerField(verbose_name='ПАЕЕРРУБ')),
                ('width_max_payeer_usd', models.IntegerField(verbose_name='ПАЕЕРДОЛЛАР')),
                ('width_max_payeer_eur', models.IntegerField(verbose_name='ПАЕЕРЕВРО')),
                ('width_max_webmoney_rub', models.IntegerField(verbose_name='ВЕБМАНИРУБ')),
                ('width_max_webmoney_usd', models.IntegerField(verbose_name='ВЕБМАНИДОЛЛАР')),
                ('width_max_webmoney_eur', models.IntegerField(verbose_name='ВЕБМАНИЕВРО')),
                ('width_max_pm_btc', models.IntegerField(verbose_name='ПМБИТКОИН')),
                ('width_max_pm_usd', models.IntegerField(verbose_name='ПМДОЛЛАР')),
                ('width_max_pm_eur', models.IntegerField(verbose_name='ПМЕВРО')),
                ('width_max_skrill_eur', models.IntegerField(verbose_name='СКРИЛЛЕВРО')),
                ('width_max_skrill_usd', models.IntegerField(verbose_name='СКРИЛДОЛЛАР')),
                ('width_max_paypal_rub', models.IntegerField(verbose_name='ПАЙПАЛРУБ')),
                ('width_max_paypal_usd', models.IntegerField(verbose_name='ПАЙПАЛДОЛЛАР')),
                ('width_max_paypal_eur', models.IntegerField(verbose_name='ПАЙПАЛЕВРО')),
                ('width_max_umoney_rub', models.IntegerField(verbose_name='ЮМАНИ')),
                ('width_max_btc', models.IntegerField(verbose_name='БИТКОИН')),
                ('width_max_xrp', models.IntegerField(verbose_name='РИПЛ')),
                ('width_max_ltc', models.IntegerField(verbose_name='ЛАЙТКОИН')),
                ('width_max_bch', models.IntegerField(verbose_name='БИТКОИНКЕШ')),
                ('width_max_xmr', models.IntegerField(verbose_name='МОНЕРО')),
                ('width_max_eth', models.IntegerField(verbose_name='ЭФИР')),
                ('width_max_etc', models.IntegerField(verbose_name='ЭФИРКЛАССИК')),
                ('width_max_dash', models.IntegerField(verbose_name='ДАШ')),
                ('width_range_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Диапазон для пополнений',
                'verbose_name_plural': 'Диапазон для пополнений',
            },
        ),
        migrations.CreateModel(
            name='RangeSumDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_min_sberbank_rub', models.IntegerField(verbose_name='СБЕРБАНК')),
                ('deposit_min_psb_rub', models.IntegerField(verbose_name='ПСБ')),
                ('deposit_min_tinkoff_rub', models.IntegerField(verbose_name='ТИНЬКОФФ')),
                ('deposit_min_gazprombank_rub', models.IntegerField(verbose_name='ГАЗПРОМБАНК')),
                ('deposit_min_alfabank_rub', models.IntegerField(verbose_name='АЛЬФАБАНК')),
                ('deposit_min_russtandart_rub', models.IntegerField(verbose_name='РУССКИЙСТАНДАРТ')),
                ('deposit_min_vtb_rub', models.IntegerField(verbose_name='ВТБ')),
                ('deposit_min_rosselhoz_rub', models.IntegerField(verbose_name='РОССЕЛЬХОЗБАНК')),
                ('deposit_min_raifaizen_rub', models.IntegerField(verbose_name='РАЙФАЙЗЕНБАНК')),
                ('deposit_min_otkritie_rub', models.IntegerField(verbose_name='ОТКРЫТИЕ')),
                ('deposit_min_pochtabank_rub', models.IntegerField(verbose_name='ПОЧТАБАНК')),
                ('deposit_min_rnkb_rub', models.IntegerField(verbose_name='РНКБ')),
                ('deposit_min_rosbank_rub', models.IntegerField(verbose_name='РОСБАНК')),
                ('deposit_min_mtsbank_rub', models.IntegerField(verbose_name='МТСБАНК')),
                ('deposit_min_qiwi_rub', models.IntegerField(verbose_name='КИВИРУБ')),
                ('deposit_min_qiwi_usd', models.IntegerField(verbose_name='КИВИДОЛЛАР')),
                ('deposit_min_payeer_rub', models.IntegerField(verbose_name='ПАЕЕРРУБ')),
                ('deposit_min_payeer_usd', models.IntegerField(verbose_name='ПАЕЕРДОЛЛАР')),
                ('deposit_min_payeer_eur', models.IntegerField(verbose_name='ПАЕЕРЕВРО')),
                ('deposit_min_webmoney_rub', models.IntegerField(verbose_name='ВЕБМАНИРУБ')),
                ('deposit_min_webmoney_usd', models.IntegerField(verbose_name='ВЕБМАНИДОЛЛАР')),
                ('deposit_min_webmoney_eur', models.IntegerField(verbose_name='ВЕБМАНИЕВРО')),
                ('deposit_min_pm_btc', models.IntegerField(verbose_name='ПМБИТКОИН')),
                ('deposit_min_pm_usd', models.IntegerField(verbose_name='ПМДОЛЛАР')),
                ('deposit_min_pm_eur', models.IntegerField(verbose_name='ПМЕВРО')),
                ('deposit_min_skrill_eur', models.IntegerField(verbose_name='СКРИЛЛЕВРО')),
                ('deposit_min_skrill_usd', models.IntegerField(verbose_name='СКРИЛДОЛЛАР')),
                ('deposit_min_paypal_rub', models.IntegerField(verbose_name='ПАЙПАЛРУБ')),
                ('deposit_min_paypal_usd', models.IntegerField(verbose_name='ПАЙПАЛДОЛЛАР')),
                ('deposit_min_paypal_eur', models.IntegerField(verbose_name='ПАЙПАЛЕВРО')),
                ('deposit_min_umoney_rub', models.IntegerField(verbose_name='ЮМАНИ')),
                ('deposit_min_btc', models.IntegerField(verbose_name='БИТКОИН')),
                ('deposit_min_xrp', models.IntegerField(verbose_name='РИПЛ')),
                ('deposit_min_ltc', models.IntegerField(verbose_name='ЛАЙТКОИН')),
                ('deposit_min_bch', models.IntegerField(verbose_name='БИТКОИНКЕШ')),
                ('deposit_min_xmr', models.IntegerField(verbose_name='МОНЕРО')),
                ('deposit_min_eth', models.IntegerField(verbose_name='ЭФИР')),
                ('deposit_min_etc', models.IntegerField(verbose_name='ЭФИРКЛАССИК')),
                ('deposit_min_dash', models.IntegerField(verbose_name='ДАШ')),
                ('deposit_max_sberbank_rub', models.IntegerField(verbose_name='СБЕРБАНК')),
                ('deposit_max_psb_rub', models.IntegerField(verbose_name='ПСБ')),
                ('deposit_max_tinkoff_rub', models.IntegerField(verbose_name='ТИНЬКОФФ')),
                ('deposit_max_gazprombank_rub', models.IntegerField(verbose_name='ГАЗПРОМБАНК')),
                ('deposit_max_alfabank_rub', models.IntegerField(verbose_name='АЛЬФАБАНК')),
                ('deposit_max_russtandart_rub', models.IntegerField(verbose_name='РУССКИЙСТАНДАРТ')),
                ('deposit_max_vtb_rub', models.IntegerField(verbose_name='ВТБ')),
                ('deposit_max_rosselhoz_rub', models.IntegerField(verbose_name='РОССЕЛЬХОЗБАНК')),
                ('deposit_max_raifaizen_rub', models.IntegerField(verbose_name='РАЙФАЙЗЕНБАНК')),
                ('deposit_max_otkritie_rub', models.IntegerField(verbose_name='ОТКРЫТИЕ')),
                ('deposit_max_pochtabank_rub', models.IntegerField(verbose_name='ПОЧТАБАНК')),
                ('deposit_max_rnkb_rub', models.IntegerField(verbose_name='РНКБ')),
                ('deposit_max_rosbank_rub', models.IntegerField(verbose_name='РОСБАНК')),
                ('deposit_max_mtsbank_rub', models.IntegerField(verbose_name='МТСБАНК')),
                ('deposit_max_qiwi_rub', models.IntegerField(verbose_name='КИВИРУБ')),
                ('deposit_max_qiwi_usd', models.IntegerField(verbose_name='КИВИДОЛЛАР')),
                ('deposit_max_payeer_rub', models.IntegerField(verbose_name='ПАЕЕРРУБ')),
                ('deposit_max_payeer_usd', models.IntegerField(verbose_name='ПАЕЕРДОЛЛАР')),
                ('deposit_max_payeer_eur', models.IntegerField(verbose_name='ПАЕЕРЕВРО')),
                ('deposit_max_webmoney_rub', models.IntegerField(verbose_name='ВЕБМАНИРУБ')),
                ('deposit_max_webmoney_usd', models.IntegerField(verbose_name='ВЕБМАНИДОЛЛАР')),
                ('deposit_max_webmoney_eur', models.IntegerField(verbose_name='ВЕБМАНИЕВРО')),
                ('deposit_max_pm_btc', models.IntegerField(verbose_name='ПМБИТКОИН')),
                ('deposit_max_pm_usd', models.IntegerField(verbose_name='ПМДОЛЛАР')),
                ('deposit_max_pm_eur', models.IntegerField(verbose_name='ПМЕВРО')),
                ('deposit_max_skrill_eur', models.IntegerField(verbose_name='СКРИЛЛЕВРО')),
                ('deposit_max_skrill_usd', models.IntegerField(verbose_name='СКРИЛДОЛЛАР')),
                ('deposit_max_paypal_rub', models.IntegerField(verbose_name='ПАЙПАЛРУБ')),
                ('deposit_max_paypal_usd', models.IntegerField(verbose_name='ПАЙПАЛДОЛЛАР')),
                ('deposit_max_paypal_eur', models.IntegerField(verbose_name='ПАЙПАЛЕВРО')),
                ('deposit_max_umoney_rub', models.IntegerField(verbose_name='ЮМАНИ')),
                ('deposit_max_btc', models.IntegerField(verbose_name='БИТКОИН')),
                ('deposit_max_xrp', models.IntegerField(verbose_name='РИПЛ')),
                ('deposit_max_ltc', models.IntegerField(verbose_name='ЛАЙТКОИН')),
                ('deposit_max_bch', models.IntegerField(verbose_name='БИТКОИНКЕШ')),
                ('deposit_max_xmr', models.IntegerField(verbose_name='МОНЕРО')),
                ('deposit_max_eth', models.IntegerField(verbose_name='ЭФИР')),
                ('deposit_max_etc', models.IntegerField(verbose_name='ЭФИРКЛАССИК')),
                ('deposit_max_dash', models.IntegerField(verbose_name='ДАШ')),
                ('deposit_range_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Диапазон для пополнений',
                'verbose_name_plural': 'Диапазон для пополнений',
            },
        ),
    ]