from django.shortcuts import render, redirect
import random

from pay.forms import RequestForm, CommissionForm
from pay.models import Transaction, CurrencyCBRF
from users.models import CustomUser


# ЗАЯВКА НА ПОПОЛНЕНИЕ ДЛЯ ОБРАБОТЧИКА
def depositwalletform(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        # получаем номер завки
        n = random.randint(1000000, 9999999)

        if form.is_valid():
            post = form.save(commit=False)
            post.request_user = request.user
            post.request_name = str(n)

            # получаем обработчика заявки
            itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника')

            # список обменников у кого хватает баланса на обработку заявки и самый лучший курс валюты
            base_comis = 100
            itemchangeset = 'None'
            for i in itemchange:
                if str(post.request_currency) == "RUB":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if i.valute_rub < base_comis:
                            itemchangeset = i.username
                            base_comis = i.valute_rub
                if str(post.request_currency) == "EUR":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if i.valute_eur < base_comis:
                            itemchangeset = i.username
                            base_comis = i.valute_eur
                if str(post.request_currency) == "USD":
                    if i.balance > post.request_sum:
                        if i.valute_usd < base_comis:
                            itemchangeset = i.username
                            base_comis = i.valute_usd

            post.request_userchange = itemchangeset
            # создаем транзакцию
            Transaction.objects.create(transaction_name=str(n),
                                       transaction_user=post.request_user,
                                       transaction_userchange=itemchangeset,
                                       transaction_type='Пополнение кошелька',
                                       transaction_status=post.request_status,
                                       transaction_currency=post.request_currency,
                                       transaction_sum=post.request_sum,
                                       transaction_sistemchange=post.request_sistemchange)
            post.save()
            return redirect('requsetwallet')
    else:
        form = RequestForm()
    return render(request, 'personalaccount/cabinet/deposit/depositwallet.html', {'form': form})


# ИЗМЕНЕНИЕ ПРИБЫЛИ ОБРАБОТЧИКА В ЛИЧНОМ КАБИНЕТЕ
def coursechangecommission(request):
    comis = CustomUser.objects.get(username=request.user)
    context = {
        'comis': comis,
        'form': CommissionForm(instance=comis),
    }
    if request.method == "POST":
        form = CommissionForm(request.POST, instance=comis)
        if form.is_valid():
            forme = form.save(commit=False)
            comis.valute_usd = forme.valute_usd
            comis.valute_rub = forme.valute_rub
            comis.valute_eur = forme.valute_eur
            comis.save()
            return redirect('coursechange')
    return render(request, 'personalaccount/cabinet/course/coursechangecommission.html', context)
