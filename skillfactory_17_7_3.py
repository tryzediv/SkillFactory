per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = input('Введите сумму, которую Вы планируете положить под проценты: ')

#Решение с циклом for
if money.isdigit():
    for profit in per_cent.values():
        deposit.append(int((int(money) * profit) / 100))
    print(deposit)
    print('Максимальная сумма, которую вы можете заработать — {}'.format(max(deposit)))
    deposit.clear()
else:
    print('Пожалуйста введите число')


#Решение без циклов
deposit.append(per_cent['ТКБ'] * int(money) / 100)
deposit.append(per_cent['СКБ'] * int(money) / 100)
deposit.append(per_cent['ВТБ'] * int(money) / 100)
deposit.append(per_cent['СБЕР'] * int(money) / 100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать — {}'.format(max(deposit)))
