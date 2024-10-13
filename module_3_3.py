def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1. Вызов функции с разным количеством аргументов
print_params()                 # Вывод: 1 строка True
print_params(10)               # Вывод: 10 строка True
print_params(10, 25)           # Вывод: 10 25 True
print_params(10, 25, False)    # Вывод: 10 25 False
print_params(b=25)             # Вывод: 1 25 True
print_params(c=[1, 2, 3])      # Вывод: 1 строка [1, 2, 3]

# 2. Создаем список и словарь и проверяем распаковку
values_list = [5.5, 'тест', False]
values_dict = {'a': 10, 'b': 'новая строка', 'c': [7, 8, 9]}

# Использование распаковки
print_params(*values_list)       # Вывод: 5.5 тест False
print_params(**values_dict)      # Вывод: 10 новая строка [7, 8, 9]

# 3. Создаем список с двумя элементами и проверяем распаковку с дополнительным параметром
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Вывод: 54.32 Строка 42
