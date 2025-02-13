"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
months_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
try:
    months_i = int(input("Введите порядковый номер месяца: "))
    if months_i >= 1 and months_i <= 12:
        print(f'{months_list[months_i - 1]}')
    else:
        print("Некорректный ввод. Повторите.")
except ValueError:
    print("Некорректный ввод. Повторите.")

#Решение через словарь
months_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
try:
    months_k = int(input("Введите порядковый номер месяца: "))
    if months_k >= 1 and months_k <= 12:
        print(f'{months_dict.get(months_k)}')
    else:
        print("Некорректный ввод. Повторите.")
except ValueError:
    print("Некорректный ввод. Повторите.")
