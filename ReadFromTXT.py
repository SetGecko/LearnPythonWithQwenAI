'''
def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()  # Читаем всё содержимое файла
        return content
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

# Пример использования функции
print(read_text_file("example.txt"))
# Вывод:
# Привет, мир!
# Это пример текстового файла.
# Мы будем его читать с помощью Python.

Открытие файла: Используем конструкцию with open(...) as file, чтобы безопасно открыть файл.
Чтение данных: Метод .read() считывает всё содержимое файла как одну строку.
Обработка ошибок: Если файла нет или у тебя нет прав на его чтение,
                  программа возвращает соответствующее сообщение об ошибке.
'''

'''
Задача 1:
Напиши функцию, которая принимает имя текстового файла и выводит количество строк в этом файле.
Подсказка: Используй метод .readlines() для считывания всех строк файла.
'''
def count_lines():
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.readlines()
            lines = 0
            for line in content:
                lines += 1
            return lines
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

print(count_lines())
'''
Задача 2:
Напиши функцию, которая принимает имя текстового файла и выводит количество слов в этом файле.
Подсказка: Раздели строки файла по пробелам с помощью метода .split().
'''
def words_count():
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            count = len(words)
            return count
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"
print(words_count())
'''
Задача 3:
Напиши функцию, которая принимает имя текстового файла и выводит самое длинное слово в файле.
Подсказка: Считай все слова, используй функцию len() для определения длины каждого слова.
'''
def the_longest_word():
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word = ""
            for el in words:
                if len(el) > len(word):
                    word = el
            return word
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"
print(the_longest_word())
'''
Задача 4:
Напиши функцию, которая принимает имя текстового файла и выводит все строки, содержащие указанное слово.
Подсказка: Проверяй каждую строку на наличие слова с помощью оператора in.
'''
def content_in_file(text_part):
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            for el in words:
                if text_part in el:
                    print(el)
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"
print(content_in_file("текст"))
print(content_in_file("Pyth"))
'''
Задача 5:
Напиши функцию, которая принимает имя текстового файла и заменяет все вхождения одного слова другим.
Подсказка: Используй метод .replace(old_word, new_word) для замены слов.
'''
def word_replace(old_word, new_word):
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.read()
            updated_content = content.replace(old_word, new_word)
        print(content)
        return f"Слово '{old_word}' успешно заменено на '{new_word}'."
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

print(word_replace("мир!", "ква"))
'''
Задача 6:
Напиши функцию, которая принимает имя текстового файла и выводит частоту встречаемости каждого слова в файле.
Подсказка: Создай словарь, где ключи — это слова, а значения — их количество.
'''
from collections import defaultdict
import re
def count_word_frequency(filename):
    word_count = defaultdict(int)
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        word_count[word] += 1
    for word, count in word_count.items():
        print(f"{word}: {count}")

count_word_frequency('example.txt')
'''
Задача 7:
Напиши функцию, которая принимает имя текстового файла и выводит только те строки, которые начинаются с указанной буквы.
Подсказка: Используй метод .startswith(letter) для проверки начала строки.
'''
def startswith(letter):
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.readlines()
            for el in content:
                if el.startswith(letter):
                    print(el)
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

print(startswith("Это"))
'''
Задача 8:
Напиши функцию, которая принимает имя текстового файла и объединяет все строки в одну, разделяя их запятой.
Подсказка: Используй метод .join() для объединения строк.
'''
def join_lines():
    try:
        with open("example.txt", "r", encoding='utf-8') as file:
            content = file.readlines()
            merged_text = ', '.join(line.strip() for line in content)
            return merged_text
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

print(join_lines())

'''
Задача 10:
Напиши функцию, которая принимает два имени файлов: исходный файл и файл для записи. 
Прочитай содержимое первого файла, преобразуй все буквы в верхний регистр и запиши результат во второй файл.
Подсказка: Используй метод .upper() для преобразования текста в верхний регистр.
'''
def change_files(old_file, new_file):
    try:
        with open(old_file, "r", encoding='utf-8') as file:
            content = file.read()
            new_content = content.upper()
        with open(new_file, "w", encoding='utf-8') as file2:
            file2.write(new_content)
    except FileNotFoundError:
        return "Ошибка: Файл не найден"
    except PermissionError:
        return "Ошибка: Нет прав доступа к файлу"

change_files("example.txt","WRexample.txt")