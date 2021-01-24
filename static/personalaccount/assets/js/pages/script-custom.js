$(document).ready(function () {
    $(document).on('keyup', 'input', function (){
        if($(this).val()<0){
            $(this).val('0.00');
        }
    });

    function readURL(input) {

        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#avatar-img').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#id_avatar").change(function(){
        readURL(this);
    });

    //ЧЕКБОКСЫ
    $.each($('.radiochekbox'), function (index, val) {
        if($(this).find('input').prop('checked')===true){
            $(this).addClass('active');
        }
    });
    $(document).on('click', '.radiochekbox', function (event) {
        $(this).parents('.card-chekbox').find('.radiochekbox').removeClass('active');
        $(this).parents('.card-chekbox').find('.radiochekbox input').prop('checked', false);
        $(this).toggleClass('active');
        $(this).find('input').prop('checked', true);
        return false;
    });
    $(document).on('click', '.btn-avatar-label', function (event) {
        $(this).toggleClass('succes');
    });
    $(document).on('click', '#chekbox-quickaplication', function () {
        $('#kriteri-fin-request-deposit').val('БЫСТРАЯ ЗАЯВКА');
    });
    $(document).on('click', '#chekbox-wincurse', function () {
        $('#kriteri-fin-request-deposit').val('ВЫГОДНЫЙ КУРС');
    });

    //ЧЕКБОКСЫ ПС
    $.each($('.block-checkbox'), function (index, val) {
       if($(this).find('input').prop('checked')===true){
           $(this).addClass('active');
       }
    });

    $(document).on('click', '.block-checkbox', function (event){
        if($(this).hasClass('active')){
            $(this).find('input').prop('checked', false);
        }else{
            $(this).find('input').prop('checked', true);
        }
        $(this).toggleClass('active')
    });

    // //КНОПКИ ПЕРЕКЛЮЧЕНИЕ РЕКВИЗИТЫ
    // $(document).on('click', '.categories-in', function (){
    //     $('.categories-in--active').addClass('categories-in').removeClass('categories-in--active');
    //     $(this).addClass('categories-in--active').removeClass('categories-in');
    //
    //     $('.form-rekvisites').toggleClass('active');
    //     $('.in-text').toggleClass('active');
    //     $('.in-box').toggleClass('active');
    //     $('.in-img-deposit').toggleClass('active');
    //     $('.in-img-withdrawal').toggleClass('active');
    // });
    //КНОПКИ СКРЫВАЮЩИЕ БЛОКИ С ПС ПОПОЛНЕНИЕ
    $(document).on('click', '#name-ps-1', function (){
        $('#card-ps-list-1').fadeToggle();
        $('#name-ps-img-1').toggleClass('transfor');
    });
    $(document).on('click', '#name-ps-2', function (){
        $('#card-ps-list-2').fadeToggle();
        $('#name-ps-img-2').toggleClass('transfor');
    });
    $(document).on('click', '#name-ps-3', function (){
        $('#card-ps-list-3').fadeToggle();
        $('#name-ps-img-3').toggleClass('transfor');
    });
    //ПОПОЛНЕНИЕ СМЕНА ЗНАЧЕНИЙ ЗАЯВКИ
    //БАНКИ
    $(document).on('click', '#sber-rub-deposit', function (){
        $('#name-fin-request-deposit').val('СБЕРБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('СБЕРБАНК')
    });
    $(document).on('click', '#tinkoff-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ТИНЬКОФФ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ТИНЬКОФФ')
    });
    $(document).on('click', '#alfabank-rub-deposit', function (){
        $('#name-fin-request-deposit').val('АЛЬФА БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('АЛЬФА БАНК')
    });
    $(document).on('click', '#vtb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ВТБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ВТБ')
    });
    $(document).on('click', '#raif-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РАЙФФАЙЗЕНБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РАЙФФАЙЗЕНБАНК')
    });
    $(document).on('click', '#otkr-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ОТКРЫТИЕ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ОТКРЫТИЕ')
    });
    $(document).on('click', '#psb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ПСБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ПСБ')
    });
    $(document).on('click', '#gazprom-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ГАЗПРОМБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ГАЗПРОМБАНК')
    });
    $(document).on('click', '#standart-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РУССКИЙ СТАНДАРТ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РУССКИЙ СТАНДАРТ')
    });
    $(document).on('click', '#rsb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РОССЕЛЬХОЗБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РОССЕЛЬХОЗБАНК')
    });
    $(document).on('click', '#roket-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РОКЕТБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РОКЕТБАНК')
    });
    $(document).on('click', '#pochta-rub-deposit', function (){
        $('#name-fin-request-deposit').val('ПОЧТА БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('ПОЧТА БАНК')
    });
    $(document).on('click', '#rosbank-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РОСБАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РОСБАНК')
    });
    $(document).on('click', '#rnkb-rub-deposit', function (){
        $('#name-fin-request-deposit').val('РНКБ');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('РНКБ')
    });
    $(document).on('click', '#mts-rub-deposit', function (){
        $('#name-fin-request-deposit').val('МТС БАНК');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('МТС БАНК')
    });
    //КОШЕЛЬКИ
    $(document).on('click', '#qiwi-rub-deposit', function (){
        $('#name-fin-request-deposit').val('QIWI RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('QIWI RUB')
    });
    $(document).on('click', '#qiwi-usd-deposit', function (){
        $('#name-fin-request-deposit').val('QIWI USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('QIWI USD')
    });
    $(document).on('click', '#payeer-rub-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('PAYEER RUB')
    });
    $(document).on('click', '#payeer-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PAYEER EUR')
    });
    $(document).on('click', '#payeer-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PAYEER USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PAYEER USD')
    });
    $(document).on('click', '#wm-rub-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('WEBMONEY RUB')
    });
    $(document).on('click', '#wm-eur-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('WEBMONEY EUR')
    });
    $(document).on('click', '#wm-usd-deposit', function (){
        $('#name-fin-request-deposit').val('WEBMONEY USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('WEBMONEY USD')
    });
    $(document).on('click', '#pm-btc-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY BTC');
        $('#val-deposit').text('BTC')
        $('#requisites-ps-name').text('PERFECT MONEY BTC')
    });
    $(document).on('click', '#pm-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PERFECT MONEY EUR')
    });
    $(document).on('click', '#pm-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PERFECT MONEY USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PERFECT MONEY USD')
    });
    $(document).on('click', '#paypal-rub-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('PAYPAL RUB')
    });
    $(document).on('click', '#paypal-eur-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('PAYPAL EUR')
    });
    $(document).on('click', '#paypal-usd-deposit', function (){
        $('#name-fin-request-deposit').val('PAYPAL USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('PAYPAL USD')
    });
    $(document).on('click', '#skrill-eur-deposit', function (){
        $('#name-fin-request-deposit').val('SKRILL EUR');
        $('#val-deposit').text('EUR')
        $('#requisites-ps-name').text('SKRILL EUR')
    });
    $(document).on('click', '#skrill-usd-deposit', function (){
        $('#name-fin-request-deposit').val('SKRILL USD');
        $('#val-deposit').text('USD')
        $('#requisites-ps-name').text('SKRILL USD')
    });
    $(document).on('click', '#umoney-rub-deposit', function (){
        $('#name-fin-request-deposit').val('UMONEY RUB');
        $('#val-deposit').text('RUB')
        $('#requisites-ps-name').text('UMONEY RUB')
    });
    // КРИПТА
    $(document).on('click', '#btc-deposit', function (){
        $('#name-fin-request-deposit').val('BITCOIN');
        $('#val-deposit').text('BTC')
        $('#requisites-ps-name').text('BITCOIN')
    });
    $(document).on('click', '#ltc-deposit', function (){
        $('#name-fin-request-deposit').val('LITECOIN');
        $('#val-deposit').text('LTC')
        $('#requisites-ps-name').text('LITECOIN')
    });
    $(document).on('click', '#xmr-deposit', function (){
        $('#name-fin-request-deposit').val('MONERO');
        $('#val-deposit').text('XMR')
        $('#requisites-ps-name').text('MONERO')
    });
    $(document).on('click', '#etc-deposit', function (){
        $('#name-fin-request-deposit').val('ETHEREUM CLASSIC');
        $('#val-deposit').text('ETC')
        $('#requisites-ps-name').text('ETHEREUM CLASSIC')
    });
    $(document).on('click', '#dash-deposit', function (){
        $('#name-fin-request-deposit').val('DASH');
        $('#val-deposit').text('DASH')
        $('#requisites-ps-name').text('DASH')
    });
    $(document).on('click', '#xrp-deposit', function (){
        $('#name-fin-request-deposit').val('RIPPLE');
        $('#val-deposit').text('XRP')
        $('#requisites-ps-name').text('RIPPLE')
    });
    $(document).on('click', '#bch-deposit', function (){
        $('#name-fin-request-deposit').val('BITCOIN CASH');
        $('#val-deposit').text('BCH')
        $('#requisites-ps-name').text('BITCOIN CASH')
    });
    $(document).on('click', '#eth-deposit', function (){
        $('#name-fin-request-deposit').val('ETHEREUM');
        $('#val-deposit').text('ETH')
        $('#requisites-ps-name').text('ETHEREUM')
    });

    $('#requisites-ps-input').keyup(function (){
        var value = $(this).val();
        $('#requisites-fin-request-deposit').val(value);
    });

    $('#input-change').keyup(function (){
        var value = $(this).val();
        if(value === ''){
            value = 0;
        }
        if(value < 0){
            value = 0;
            $(this).val('')
        }
        $('#sum-fin-request-deposit').val(value);
    });

// РЕЗЕРВ МЕНЯЕМ НА ноль при загрузке
    $.each($('.block-reserv'), function (index, val) {
       if($(this).find('input').val()==='0E-8'){
           $(this).find('input').val('0.00000000');
       }
    });
});




//МАСКА НА ИНПУТ ДЛЯ ВВОДА КАРТЫ
$(document).ready(function () {
    var cleavecard = new Cleave('#input-card', {
        creditCard: true,
    });
});
