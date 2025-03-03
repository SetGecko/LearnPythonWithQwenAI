'''
Метод класса — это специальный тип метода, который привязан к самому классу, а не к его экземплярам.
Он используется для выполнения операций, которые влияют на весь класс или создают новые объекты этого класса.

Ключевые особенности:
Декоратор @classmethod:
Метод класса определяется с помощью декоратора @classmethod.
Первый параметр — ссылка на класс (cls):
Вместо self (ссылки на объект), первый параметр метода класса — это cls, которая указывает на сам класс.
Использование:
Для создания альтернативных конструкторов.
Для выполнения операций с атрибутами самого класса (например, подсчет количества объектов).

Пример метода класса
Задача: Создание альтернативного конструктора
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # Вычисляем возраст на основе года рождения
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age)  # Создаем объект класса Person

# Создаем объекты через обычный конструктор
person1 = Person("Алексей", 37)
print(person1.name, person1.age)  # Вывод: Алексей 37

# Создаем объект через метод класса
person2 = Person.from_birth_year("Мария", 1998)
print(person2.name, person2.age)  # Вывод: Мария 25

Что здесь происходит?
Метод from_birth_year() — это метод класса, который вычисляет возраст на основе года рождения и создает новый объект класса Person.
Мы используем cls для вызова конструктора (__init__) внутри метода класса.

Когда использовать методы класса?
Альтернативные конструкторы:
Если у тебя есть несколько способов создания объекта, можно использовать методы класса. Например:
Создание человека по имени и возрасту.
Создание человека по имени и году рождения.
Работа с атрибутами класса:
Методы класса могут изменять или использовать атрибуты самого класса, а не конкретных объектов.
Фабричные методы:
Методы класса часто используются как "фабричные методы" для создания объектов с определенными свойствами.

Пример работы с атрибутами класса
Задача: Подсчет количества объектов

class Car:
    total_cars = 0  # Атрибут класса для подсчета машин

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1  # Увеличиваем счетчик при создании каждого объекта

    @classmethod
    def get_total_cars(cls):
        return f"Общее количество машин: {cls.total_cars}"  # Используем атрибут класса

# Создаем объекты
car1 = Car("Daewoo Nexia")
car2 = Car("Toyota Corolla")

# Получаем общее количество машин
print(Car.get_total_cars())  # Вывод: Общее количество машин: 2

Что здесь происходит?
Атрибут total_cars принадлежит самому классу Car, а не его объектам.
Метод класса get_total_cars() использует cls.total_cars для доступа к атрибуту класса.

Преимущества методов класса
Глобальная логика:
Методы класса позволяют работать с глобальными данными класса, а не с данными конкретных объектов.
Создание объектов:
Методы класса удобно использовать для создания объектов с определенными параметрами.
Чистота кода:
Если метод относится ко всем объектам класса, лучше сделать его методом класса, чем обычным методом.

Пример использования метода класса
Задача: Создание книг разных форматов

class Book:
    def __init__(self, title, author, format):
        self.title = title
        self.author = author
        self.format = format

    @classmethod
    def create_ebook(cls, title, author):
        return cls(title, author, "PDF")  # Создаем электронную книгу

    @classmethod
    def create_paperbook(cls, title, author):
        return cls(title, author, "Paper")  # Создаем печатную книгу


# Создаем книги через методы класса
ebook = Book.create_ebook("Пикник на обочине", "Братья Стругацкие")
paperbook = Book.create_paperbook("Гиперион", "Дэн Симонс")

# Вывод информации
print(ebook.title, ebook.author, ebook.format)  # Вывод: Пикник на обочине Братья Стругацкие PDF
print(paperbook.title, paperbook.author, paperbook.format)  # Вывод: Гиперион Дэн Симонс Paper
'''

'''
Задача 1: Автомобиль
Алгоритм:
Создай класс Car, который хранит общее количество автомобилей (total_cars).
Определи метод класса create_car(brand) с помощью декоратора @classmethod.
Увеличь счетчик total_cars на 1.

Создай объект класса Car с указанным брендом (brand) и верни его.
Определи метод get_total_cars(), который возвращает текущее значение total_cars.
'''
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return f"Общее количество машин: {cls.total_cars}"

car1 = Car("Daewoo Nexia")
car2 = Car("Toyota Corolla Levin")
print(Car.total_cars)
'''
Задача 2: Пользователь
Алгоритм:
Создай класс User, который хранит общее количество пользователей (total_users).
Определи метод класса create_user(name) с помощью декоратора @classmethod.
Увеличь счетчик total_users на 1.
Создай объект класса User с указанным именем (name) и верни его.
Определи метод get_total_users(), который возвращает текущее значение total_users.
'''
class User:
    total_users = 0

    def __init__(self, name):
        self.name = name
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return f"Всего пользователей: {User.total_users}"

user1 = User("Алексей")
user2 = User("Qwen")
print(User.total_users)
'''
Задача 3: Книга
Алгоритм:
Создай класс Book, который хранит общее количество книг (total_books).
Определи метод класса create_book(title) с помощью декоратора @classmethod.
Увеличь счетчик total_books на 1.
Создай объект класса Book с указанным названием (title) и верни его.
Определи метод get_total_books(), который возвращает текущее значение total_books.
'''
class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):
        return Book.total_books

b1 = Book("Hypireon")
b2 = Book("Architect")
print(Book.total_books)
'''
Задача 4: Город
Алгоритм:
Создай класс City, который хранит общее количество городов (total_cities).
Определи метод класса create_city(name) с помощью декоратора @classmethod.
Увеличь счетчик total_cities на 1.
Создай объект класса City с указанным названием (name) и верни его.
Определи метод get_total_cities(), который возвращает текущее значение total_cities.
'''
class City:
    total_cities = 0

    def __init__(self, name):
        self.name = name
        City.total_cities += 1

    @classmethod
    def get_total_cities(cls):
        return City.total_cities

c1 = City("Moscow")
c2 = City("Krasnodar")
c3 = City("Timashevsk")
print(City.get_total_cities())
'''
Задача 5: Фильм
Алгоритм:
Создай класс Film, который хранит общее количество фильмов (total_films).
Определи метод класса create_film(title) с помощью декоратора @classmethod.
Увеличь счетчик total_films на 1.
Создай объект класса Film с указанным названием (title) и верни его.
Определи метод get_total_films(), который возвращает текущее значение total_films.
'''
class Film:
    total_films = 0

    def __init__(self, title):
        self.title = title
        Film.total_films += 1

    @classmethod
    def get_total_films(cls):
        return Film.total_films

f1 = Film("Alien")
print(Film.get_total_films())
'''
Задача 6: Телефон
Алгоритм:
Создай класс Phone, который хранит общее количество телефонов (total_phones).
Определи метод класса create_phone(number) с помощью декоратора @classmethod.
Увеличь счетчик total_phones на 1.
Создай объект класса Phone с указанным номером (number) и верни его.
Определи метод get_total_phones(), который возвращает текущее значение total_phones.
'''
class Phone:
    total_phones = 0

    def __init__(self, number):
        self.number = number
        Phone.total_phones += 1

    @classmethod
    def get_total_phones(cls):
        return Phone.total_phones

p1 = Phone("iPhone")
p2 = Phone("Xiaomi")
print(Phone.get_total_phones())
'''
Задача 7: Банковский счет
Алгоритм:
Создай класс BankAccount, который хранит процентную ставку (interest_rate) как атрибут класса.
Определи метод класса set_interest_rate(new_rate) с помощью декоратора @classmethod.
Измени значение interest_rate на новое (new_rate).
Определи метод calculate_interest(balance), который:
Принимает баланс (balance).
Вычисляет проценты как balance * interest_rate / 100.
'''
class BankAccount:
    interest_rate = 0  # Атрибут класса

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    def __init__(self, balance):
        self.balance = balance
        self.interest_rate = BankAccount.interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


b1 = BankAccount(1000)
BankAccount.set_interest_rate(20)
print(b1.interest_rate)
print(b1.calculate_interest())
'''
Задача 8: Человек
Алгоритм:
Создай класс Person, который хранит общее количество людей (total_people).
Определи метод класса create_person(name) с помощью декоратора @classmethod.
Увеличь счетчик total_people на 1.
Создай объект класса Person с указанным именем (name) и верни его.
Определи метод get_total_people(), который возвращает текущее значение total_people.
'''
class Person:
    total_people = 0

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    @classmethod
    def get_total_people(cls):
        return Person.total_people
p1 = Person("Alexey")
p2 = Person("Anna")
print(Person.get_total_people())
'''
Задача 9: Магазин
Алгоритм:
Создай класс Store, который хранит общее количество магазинов (total_stores).
Определи метод класса create_store(name) с помощью декоратора @classmethod.
Увеличь счетчик total_stores на 1.
Создай объект класса Store с указанным названием (name) и верни его.
Определи метод get_total_stores(), который возвращает текущее значение total_stores.
'''
class Store:
    total_stores = 0

    def __init__(self, name):
        self.name = name
        Store.total_stores += 1

    @classmethod
    def get_total_stores(cls):
        return Store.total_stores

st1 = Store("Magnit")
st2 = Store("Lenta")
print(Store.get_total_stores())
'''
Задача 10: Кофемашина
Алгоритм:
Создай класс CoffeeMachine, который хранит общее количество кофемашин (total_machines).
Определи метод класса create_machine(model) с помощью декоратора @classmethod.
Увеличь счетчик total_machines на 1.
Создай объект класса CoffeeMachine с указанным моделью (model) и верни его.
Определи метод get_total_machines(), который возвращает текущее значение total_machines.
'''
class CoffeeMachine:
    total_machines = 0

    def __init__(self, model):
        self.model = model
        CoffeeMachine.total_machines += 1

    @classmethod
    def get_total_machines(cls):
        return CoffeeMachine.total_machines

cm1 = CoffeeMachine("Indesit")
cm2 = CoffeeMachine("Ariston")
cm3 = CoffeeMachine("Nescafe")
cm4 = CoffeeMachine("Bosch")
print(CoffeeMachine.get_total_machines())