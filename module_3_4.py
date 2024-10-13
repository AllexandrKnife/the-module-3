def single_root_words(root_word, *other_words):
    # Создаем пустой список same_words для хранения подходящих слов
    same_words = []
    # Приводим root_word к нижнему регистру для удобства сравнения
    root_word_lower = root_word.lower()

    # Перебираем все слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в текущем слове или текущее слово в root_word
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Если условие выполняется, добавляем слово в список same_words
            same_words.append(word)

    # Возвращаем список same_words
    return same_words

# Вызываем функцию single_root_words с разными аргументами и сохраняем результаты
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты на экран
print(result1)
print(result2)