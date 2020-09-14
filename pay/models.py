from django.db import models
from django.urls import reverse
from django.utils import timezone


class Transaction(models.Model):
    date_joined_change = models.DateTimeField('Заявка создана', default=timezone.now)
    transaction_name = models.CharField('Название транзакции', max_length=150)
    transaction_user = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, default=1,
                                         verbose_name='Логин пользователя')
    transaction_type = models.CharField('Тип транзакции', max_length=150, default="выполнена")
    transaction_status = models.CharField('Статус', max_length=150, default="выполнена")
    transaction_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1,
                                             verbose_name='Валюта')
    transaction_sum = models.DecimalField('Сумма', default=0.00, max_digits=10, decimal_places=2)
    transaction_sistemchange = models.ForeignKey('SistemChange', on_delete=models.PROTECT, default=1,
                                                 verbose_name='Платежная система')

    def __str__(self):
        return self.transaction_name

    class Meta:
        verbose_name = 'Транзакцию'
        verbose_name_plural = 'Транзакции'


class Currency(models.Model):
    base_currency = models.CharField('Валюта', db_index=True, max_length=150)

    def __str__(self):
        return self.base_currency

    class Meta:
        verbose_name = 'Валюту'
        verbose_name_plural = 'Валюты'


class SistemChange(models.Model):
    base_sistemchange = models.CharField('Платежная система', db_index=True, max_length=150)

    def __str__(self):
        return self.base_sistemchange

    class Meta:
        verbose_name = 'Платежную систему'
        verbose_name_plural = 'Платежные системы'


class RequestChange(models.Model):
    request_userchange = models.CharField('Обработчик заявки', max_length=150, blank=True)
    date_joined_change = models.DateTimeField('Дата создания', default=timezone.now)
    request_name = models.CharField('Название заявки', max_length=150)
    request_user = models.CharField('Логин пользователя', max_length=150)
    request_status = models.CharField('Статус заявки', max_length=150, default="В обработке")
    request_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1,
                                         verbose_name='Валюта')
    request_sum = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    request_sistemchange = models.ForeignKey('SistemChange', on_delete=models.PROTECT, default=1,
                                             verbose_name='Платежная система')

    def get_absolute_url(self):
        return reverse('depositexchangerequest', kwargs={"pk": self.pk})

    def __str__(self):
        return self.request_name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
