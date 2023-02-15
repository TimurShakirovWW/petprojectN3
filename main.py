amount = int(input('Сколько роликов выпущено в этом месяце?'))
total = 0
views_payment = 2.2
for i in range(amount):
    views = int(input('Количество просмотров ' + str(i+1) +'-го ролика'))
    total += views//1000 * views_payment
    advt = input('Была ли в ролике рекламная интеграция (да/нет)?').lower()
    if advt == 'да':
        advt_payment = int(input('Введите стоимость интеграции'))
        total += advt_payment
total = int(total)
print('Заработано за месяц:', total, 'USD.')
