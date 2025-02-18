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
import csv
class User:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    def get_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Студент: {self.is_student}"

users_list = []

with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        user = User(row[0], row[1], row[2])
        users_list.append(user)

for user in users_list:
    print(user.get_info())
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
import csv

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return "Информация о книге"

class Ebook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format

    def get_info(self):
        return f"Электронная книга: {self.title}, Автор: {self.author}, Формат: {self.format}"

# Определяем класс PaperBook
class PaperBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def get_info(self):
        return f"Печатная книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


books = []

with open("books.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get("format"):
            ebook = Ebook(row["title"], row["author"], row["format"])
            books.append(ebook)
        elif row.get("pages"):
            paperbook = PaperBook(row["title"], row["author"], int(row["pages"]))
            books.append(paperbook)

for book in books:
    print(book.get_info())
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
import csv
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def get_info(self):
        return "Информация о машине"

class Sedan(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)
    def get_info(self):
        return f"Легковой автомобиль: {self.brand}, Год: {self.year}"

class Truck(Car):
    def __init__(self, brand, year, load_capacity):
        super().__init__(brand, year)
        self.load_capacity = load_capacity
    def get_info(self):
        return f"Грузовик: {self.brand}, Год: {self.year}, Грузоподъемность: {self.load_capacity}"

class Van(Car):
    def __init__(self, brand, year, load_capacity):
        super().__init__(brand, year)
        self.load_capacity = load_capacity
    def get_info(self):
        return f"Фургон: {self.brand}, Год: {self.year}, Грузоподъемность: {self.load_capacity}"

cars = []

with open("cars.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get("type") == "sedan":
            sedan = Sedan(row["brand"], int(row["year"]))
            cars.append(sedan)
        elif row.get("type") == "van":
            van = Van(row["brand"], int(row["year"]), int(row["load_capacity"]))
            cars.append(van)
        elif row.get("type") == "truck":
            truck = Truck(row["brand"], int(row["year"]), int(row["load_capacity"]))
            cars.append(truck)

for car in cars:
    print(car.get_info())
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
import csv

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_info(self):
        return "Информация о городе"

class Capital(City):
    def __init__(self, name, population, country, is_capital):
        super().__init__(name, population)
        self.country = country
        self.is_capital = is_capital

    def get_info(self):
        return f"Столица: {self.name}, Население: {self.population}, Страна: {self.country}, Столица: {self.is_capital}"

class SmallCity(City):
    def __init__(self, name, population):
        super().__init__(name, population)
    def get_info(self):
        return f"Город: {self.name}, Население: {self.population}"


cities = []

with open("cities.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get("is_capital") == "True":
            capital = Capital(row["name"], int(row["population"]), row["country"], row["is_capital"])
            cities.append(capital)
        elif row.get("is_capital") == "False":
            small = SmallCity(row["name"], int(row["population"]))
            cities.append(small)

for el in cities:
    print(el.get_info())
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
import csv
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return f"Баланс = {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        lim = (self.balance / 100) * 90
        if amount <= lim:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"
        else:
            return "Нельзя снять больше 90% баланса"

class CreditCard(BankAccount):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.limit or amount > self.balance:
            return "Операция невозможна"
        else:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"

cards = []

with open("accounts.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get("type") == "savings":
            sav = SavingsAccount(int(row["balance"]), int(row["interest_rate"]))
            cards.append(sav)
        elif row.get("type") == "credit_card":
            cc = CreditCard(int(row["balance"]), int(row["limit"]))
            cards.append(cc)

for el in cards:
    print(el.withdraw(1000))