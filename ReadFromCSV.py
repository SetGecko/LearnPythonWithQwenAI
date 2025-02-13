'''
Как читать и писать CSV-файлы в Python?
Для работы с CSV в Python используется модуль csv. Вот основные шаги:
Импортируем модуль:
import csv
Чтение из CSV-файла:
Открываем файл с помощью open() в режиме "r" (чтение).
Используем csv.reader() или csv.DictReader() для чтения данных.
Запись в CSV-файл:
Открываем файл с помощью open() в режиме "w" (запись).
Используем csv.writer() или csv.DictWriter() для записи данных.

Пример: Чтение из CSV-файла
CSV-файл (users.csv):
name,age,is_student
Алексей,37,False
Мария,25,True
Иван,19,True

Python-код:
import csv

# Открываем CSV-файл для чтения
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Читаем файл как словарь
    for row in reader:
        print(f"Имя: {row['name']}, Возраст: {row['age']}, Студент: {row['is_student']}")


Основные методы модуля csv:
csv.reader(file) :
Читает CSV-файл как список строк.
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row — это список значений

csv.DictReader(file) :
Читает CSV-файл как словарь, используя первую строку как ключи.
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"], row["is_student"])

csv.writer(file) :
Записывает данные в CSV-файл как список строк.
data = [["name", "age", "is_student"], ["Алексей", 37, False], ["Мария", 25, True]]
with open("users.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

csv.DictWriter(file, fieldnames) :
Записывает данные в CSV-файл как словарь.
data = [{"name": "Алексей", "age": 37, "is_student": False}]
with open("users.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "is_student"])
    writer.writeheader()
    writer.writerows(data)


Особенности работы с CSV
Разделители:
По умолчанию csv использует запятую , как разделитель. Если в файле используется другой разделитель (например, точка с запятой ;), укажи его явно:
python
Copy
1
reader = csv.reader(file, delimiter=";")
Кодировка:
Всегда указывай кодировку encoding="utf-8", чтобы избежать проблем с русскими символами.
Обработка ошибок:
Иногда CSV-файл может быть поврежден или иметь неправильную структуру. Обрабатывай такие ситуации с помощью блока try-except.
Работа с большими файлами:
Если файл очень большой, используй цикл for для построчного чтения, чтобы не загружать всё содержимое в память.


'''

'''
Задача 1: Информация о пользователях
Алгоритм:
Создай класс User, который будет хранить имя (name), возраст (age) и статус студента (is_student).
Определи метод get_info(), который возвращает строку формата:
"Имя: [name], Возраст: [age], Студент: [is_student]".
Используй модуль csv для чтения файла users.csv.
Создай список объектов класса User на основе данных из файла.
Вызови метод get_info() для каждого объекта и выведи результат.
'''

'''
Задача 2: Список книг
Алгоритм:
Создай базовый класс Book, который хранит название (title) и автора (author).
Создай дочерний класс Ebook, унаследованный от Book. Добавь атрибут format.
Создай дочерний класс PaperBook, унаследованный от Book. Добавь атрибут pages.
Определи метод get_info() для каждого класса:
Для Ebook: "Электронная книга: [title], Автор: [author], Формат: [format]".
Для PaperBook: "Печатная книга: [title], Автор: [author], Страниц: [pages]".
Используй модуль csv для чтения файла books.csv.
Создай список объектов (Ebook или PaperBook в зависимости от наличия ключей format или pages).
Вызови метод get_info() для каждого объекта и выведи результат.
'''

'''
Задача 3: Автопарк
Алгоритм:
Создай базовый класс Car, который хранит марку (brand) и год выпуска (year).
Создай дочерний класс Sedan, унаследованный от Car.
Создай дочерний класс Truck, унаследованный от Car. Добавь атрибут load_capacity.
Создай дочерний класс Van, унаследованный от Car. Добавь атрибут load_capacity.
Определи метод get_info() для каждого класса:
Для Sedan: "Легковой автомобиль: [brand], Год: [year]".
Для Truck: "Грузовик: [brand], Год: [year], Грузоподъемность: [load_capacity]".
Для Van: "Фургон: [brand], Год: [year], Грузоподъемность: [load_capacity]".
Используй модуль csv для чтения файла cars.csv.
Создай список объектов (Sedan, Truck или Van в зависимости от типа автомобиля).
Вызови метод get_info() для каждого объекта и выведи результат.
'''

'''
Задача 4: Города
Алгоритм:
Создай базовый класс City, который хранит название (name) и население (population).
Создай дочерний класс Capital, унаследованный от City. Добавь атрибуты country и is_capital.
Создай дочерний класс SmallCity, унаследованный от City.
Определи метод get_info() для каждого класса:
Для Capital: "Столица: [name], Население: [population], Страна: [country], Столица: [is_capital]".
Для SmallCity: "Город: [name], Население: [population]".
Используй модуль csv для чтения файла cities.csv.
Создай список объектов (Capital или SmallCity в зависимости от значения is_capital).
Вызови метод get_info() для каждого объекта и выведи результат.
'''

'''
Задача 5: Банковские счета
Алгоритм:
Создай базовый класс BankAccount, который хранит баланс (balance).
Создай дочерний класс SavingsAccount, унаследованный от BankAccount. Добавь атрибут interest_rate.
Создай дочерний класс CreditCard, унаследованный от BankAccount. Добавь атрибут limit.
Определи метод withdraw(amount) для каждого класса:
Для SavingsAccount: нельзя снять больше 90% баланса.
Для CreditCard: нельзя снять сумму, превышающую лимит (limit) или доступный баланс.
Используй модуль csv для чтения файла accounts.csv.
Создай список объектов (SavingsAccount или CreditCard в зависимости от типа счета).
Вызови метод withdraw(amount) для каждого объекта с заданной суммой (например, 1000) и выведи результат.
'''