'''
json.load(file) :
Считывает содержимое JSON-файла и преобразует его в Python-объект (словарь или список).
json.dump(data, file) :
Записывает Python-объект (словарь или список) в JSON-файл.
json.loads(json_string) :
Преобразует JSON-строку в Python-объект.
json.dumps(data) :
Преобразует Python-объект в JSON-строку.

import json

# Открываем JSON-файл для чтения
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Преобразуем содержимое файла в Python-объект

# Работаем с данными
print(data["name"])       # Вывод: Алексей
print(data["age"])        # Вывод: 37
print(data["skills"])     # Вывод: ['Python', 'SQL', 'Git']
print(data["is_student"]) # Вывод: False
'''

'''
Задача 1: Информация о пользователе
Описание: У тебя есть JSON-файл user.json с данными о пользователе

Алгоритм:

Создай класс User, который будет хранить данные о пользователе.
В методе __init__ сохрани параметры name, age, is_student и skills.
Напиши метод get_info(), который возвращает строку формата:
"Имя: [name], Возраст: [age], Студент: [is_student], Навыки: [skills]".
Прочитай файл user.json и создай объект класса User.
Вызови метод get_info().
'''
import json
class User:
    def __init__(self, name, age, is_student, skills):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.skills = skills
    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Студент: {self.is_student}, Навыки: {self.skills}"


with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)

me = User(data["name"],data["age"], data["is_student"], data["skills"])
print(me.get_info())
'''
Задача 2: Список книг
Описание: У тебя есть JSON-файл books.json со списком книг
Алгоритм:

Создай базовый класс Book, который хранит название (title) и автора (author).
Создай дочерний класс Ebook, унаследованный от Book. Добавь атрибут format.
Создай дочерний класс PaperBook, унаследованный от Book. Добавь атрибут pages.

Определи метод get_info() для каждого класса, чтобы он возвращал разные строки:
Для Ebook: "Электронная книга: [title], Автор: [author], Формат: [format]".
Для PaperBook: "Печатная книга: [title], Автор: [author], Страниц: [pages]".
Прочитай файл books.json и создай список объектов (Ebook или PaperBook в зависимости от данных).
Вызови метод get_info() для каждого объекта.
'''
import  json

with open("books.json", "r", encoding="utf-8") as file:
    data = json.load(file)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return "Информация о книге"

class Ebook(Book):
    def __init__(self, title, author, format):
        super().__init__(author, title)
        self.format = format
    def get_info(self):
        return f"Электронная книга: {self.title}, Автор: {self.author}, Формат: {self.format}"

class PaperBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    def get_info(self):
        return f"Электронная книга: {self.title}, Автор: {self.author}, Формат: {self.pages}"

books_list = []

for book_data in data:
    if "format" in book_data:
        eb = Ebook(book_data["title"], book_data["author"], book_data["format"])
        books_list.append(eb)
    elif "pages" in book_data:
        pb = PaperBook(book_data["title"], book_data["author"], book_data["pages"])
        books_list.append(pb)

for book in books_list:
    print(book.get_info())
'''
Задача 3: Автопарк
Описание: У тебя есть JSON-файл cars.json с данными об автомобилях
Алгоритм:

Создай базовый класс Car, который хранит марку (brand) и год выпуска (year).
Создай дочерний класс Sedan, унаследованный от Car.
Создай дочерний класс Truck, унаследованный от Car. Добавь атрибут load_capacity.
Определи метод get_info() для каждого класса, чтобы он возвращал разные строки:
Для Sedan: "Легковой автомобиль: [brand], Год: [year]".
Для Truck: "Грузовик: [brand], Год: [year], Грузоподъемность: [load_capacity]".
Прочитай файл cars.json и создай список объектов (Sedan или Truck в зависимости от типа).
Вызови метод get_info() для каждого объекта.
'''
import json

with open("cars.json", "r", encoding="utf-8") as file:
    data = json.load(file)

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def get_info(self):
        return "Информация об автомобиле"

class Sedan(Car):
    def __init__(self,  brand, year):
        super().__init__(brand, year)
    def get_info(self):
        return f"Легковой автомобиль: {self.brand}, Год: {self.year}"

class Truck(Car):
    def __init__(self,  brand, year, load_capacity):
        super().__init__(brand, year)
        self.load_capacity = load_capacity
    def get_info(self):
        return f"Грузовик: {self.brand}, Год: {self.year}, Грузоподъемность: {self.load_capacity}"

cars = []

for car_data in data:
    if "load_capacity" in car_data:
        eb = Truck(car_data["brand"], car_data["year"], car_data["load_capacity"])
        cars.append(eb)
    else:
        pb = Sedan(car_data["brand"], car_data["year"])
        cars.append(pb)

for car in cars:
    print(car.get_info())
'''
Задача 4: Города
Описание: У тебя есть JSON-файл cities.json с данными о городах
Алгоритм:

Создай базовый класс City, который хранит название (name) и население (population).
Создай дочерний класс Capital, унаследованный от City. Добавь атрибут country.
Создай дочерний класс SmallCity, унаследованный от City.
Определи метод get_info() для каждого класса, чтобы он возвращал разные строки:
Для Capital: "Столица: [name], Население: [population], Страна: [country]".
Для SmallCity: "Город: [name], Население: [population]".
Прочитай файл cities.json и создай список объектов (Capital или SmallCity в зависимости от значения is_capital).
Вызови метод get_info() для каждого объекта.
'''
import json

with open("cities.json", "r", encoding="utf-8") as file:
    data = json.load(file)

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_info(self):
        return "Информация о городе"

class Capital(City):
    def __init__(self, name, population, country):
        super().__init__(name, population)
        self.country = country

    def get_info(self):
        return f"Столица: {self.name}, Население: {self.population}, Страна: {self.country}"

class SmallCity(City):
    def __init__(self, name, population):
        super().__init__(name, population)

    def get_info(self):
        return f"Город: {self.name}, Население: {self.population}"

cities = []

for c in data:
    if c.get("is_capital", False):
        capital = Capital(c["name"], c["population"], c["country"])
        cities.append(capital)
    else:
        small_city = SmallCity(c["name"], c["population"])
        cities.append(small_city)


for city in cities:
    print(city.get_info())
'''
Задача 5: Банковские счета
Описание: У тебя есть JSON-файл accounts.json с данными о счетах
Алгоритм:

Создай базовый класс BankAccount, который хранит баланс (balance).
Создай дочерний класс SavingsAccount, унаследованный от BankAccount. Добавь атрибут interest_rate.
Создай дочерний класс CreditCard, унаследованный от BankAccount. Добавь атрибут limit.
Определи метод withdraw(amount) для каждого класса:
Для SavingsAccount: нельзя снять больше 90% баланса.
Для CreditCard: нельзя снять сумму превышающую лимит.
Прочитай файл accounts.json и создай список объектов (SavingsAccount или CreditCard в зависимости от типа).
Вызови метод withdraw(amount) для каждого объекта.
'''
import json

# Чтение JSON-файла
with open("accounts.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # data — это список словарей


# Базовый класс BankAccount
class BankAccount:
    def __init__(self, balance):
        self.balance = balance


# Дочерний класс SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        lim = (self.balance / 100) * 90  # Максимум 90% баланса
        if amount <= lim:  # Проверяем лимит
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"
        else:
            return "Нельзя снять больше 90% баланса"


# Дочерний класс CreditCard
class CreditCard(BankAccount):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.limit or amount > self.balance:  # Проверяем лимит и баланс
            return "Операция невозможна"
        else:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"


# Создаем список объектов
bank_accounts = []

for b in data:  # Проходим по каждому элементу списка
    if b.get("type") == "savings":  # Проверяем тип счета
        sa = SavingsAccount(b["balance"], b["interest_rate"])
        bank_accounts.append(sa)
    elif b.get("type") == "credit_card":  # Проверяем тип счета
        cc = CreditCard(b["balance"], b["limit"])
        bank_accounts.append(cc)

# Вызываем метод withdraw() для каждого объекта
for account in bank_accounts:
    print(account.withdraw(1000))