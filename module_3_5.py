def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Берем первую цифру и преобразуем её в число
        first = int(str_number[0])
        # Рекурсивно вызываем функцию для оставшейся части числа и умножаем на первую цифру
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась одна цифра, возвращаем её
        return int(str_number)

# Вызываем функцию и выводим результат
result = get_multiplied_digits(40203)
print(result)