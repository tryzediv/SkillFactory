try:
    # Запрос на количество билетов
    tickets = int(input('Сколько билетов Вы хотите купить?\n'))
    #Формируем список с билетами
    tickets_list = [i + 1 for i in range(tickets)]
    #Запрашиваем возраст для каждого билета, стоимость билетов сохраняем в список
    result = []

    for ticket in tickets_list:
        age = int(input('Сколько лет посетителю с билетом №{}\n'.format(ticket)))
        if age < 18:
            result.append(0)
        elif age < 25:
            result.append(990)
        else:
            result.append(1390)

    #Выводим сумму к оплате, учитывая скидку, если больше 3х билетов
    if len(result) > 3:
        sale = sum(result) * 10 / 100
        print('Сумма к оплате: {} руб.'.format(sum(result) - sale))
    else:
        print('Сумма к оплате: {} руб.'.format(sum(result)))
except ValueError:
    print('Пожалуйста вводите целые числа')
