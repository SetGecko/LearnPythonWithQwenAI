'''
Задача 1: Класс для животного
Напиши класс Animal, который будет иметь метод say_sound(). Этот метод должен выводить строку "Гав!" для собаки.
Алгоритм:
Создай класс Animal.
Определи метод say_sound().
В методе используй print("Гав!").
'''
class Animal:
    def say_sound(self):
        return "Гав"


dog = Animal()
print(dog.say_sound())
'''
Задача 2: Класс для числа
Напиши класс Number, который будет хранить число. Метод get_number() должен возвращать это число.
Алгоритм:
Создай класс Number.
В методе __init__ сохрани число как атрибут объекта.
Определи метод get_number(), который вернет сохраненное число.
'''
class Number:
    def __init__(self, num):
        self.num = num
    def get_number(self):
        print(self.num)


number = Number(4)
number.get_number()
'''
Задача 3: Класс для кошки
Напиши класс Cat, который будет иметь метод say_meow(). Этот метод должен выводить строку "Мяу!".
Алгоритм:
Создай класс Cat.
Определи метод say_meow().
Выведи строку "Мяу!".
'''
class Cat:
    def say_meow(self):
        return "Мяу!"


cat = Cat()
print(cat.say_meow())
'''
Задача 4: Класс для цвета
Напиши класс Color, который будет хранить название цвета. Метод get_color() должен возвращать это название.
Алгоритм:
Создай класс Color.
В методе __init__ сохрани название цвета как атрибут объекта.
Определи метод get_color(), который вернет название цвета.
'''
class Color:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        print(self.color)


color = Color("Зелёный")
color.get_color()
'''
Задача 5: Класс для машины
Напиши класс Car, который будет хранить модель машины. Метод start_engine() должен выводить строку "Двигатель запущен".
Алгоритм:
Создай класс Car.
В методе __init__ сохрани модель машины как атрибут объекта.
Определи метод start_engine(), который выведет строку "Двигатель запущен".
'''
class Car:
    def __init__(self, model):
        self.model = model
    def start_engine(self):
        print(f"Дивгатель {self.model} запущен")


car = Car("Daewoo Nexia")
car.start_engine()
'''
Задача 6: Класс для города
Напиши класс City, который будет хранить название города. Метод get_name() должен возвращать название.
Алгоритм:
Создай класс City.
В методе __init__ сохрани название города как атрибут объекта.
Определи метод get_name(), который вернет название города.
'''
class City:
    def __init__(self, city_name):
        self.city_name = city_name
    def get_name(self):
        print(self.city_name)


city = City("Краснодар")
city.get_name()
'''
Задача 7: Класс для времени
Напиши класс Time, который будет хранить часы и минуты. Метод get_time() должен возвращать время в формате "12:30".
Алгоритм:
Создай класс Time.
В методе __init__ сохрани часы и минуты как атрибуты объекта.
Определи метод get_time(), который вернет строку в формате "чч:мм".
'''
class Time:
    def __init__(self,time):
        self.time = time
    def get_time(self):
        print(self.time)


time = Time("18:30")
time.get_time()
'''
Задача 8: Класс для точки
Напиши класс Point, который будет хранить координаты x и y. Метод get_coordinates() должен возвращать кортеж (x, y).
Алгоритм:
Создай класс Point.
В методе __init__ сохрани координаты x и y как атрибуты объекта.
Определи метод get_coordinates(), который вернет (self.x, self.y).
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_coordinates(self):
        print(f"{self.x}, {self.y}")


point = Point(4, 3)
point.get_coordinates()
'''
Задача 9: Класс для прямоугольника (дополнительный метод)
Напиши класс Rectangle, который будет хранить ширину (width) и высоту (height). 
Добавь метод get_perimeter(), который возвращает периметр прямоугольника.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани ширину и высоту как атрибуты объекта.
Определи метод get_perimeter(), который вернет 2 * (self.width + self.height).
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_perimeter(self):
        print(f"{2 * (self.width + self.height)}")


rect = Rectangle(4, 2)
rect.get_perimeter()
'''
Задача 10: Класс для круга
Напиши класс Circle, который будет хранить радиус (radius). Добавь метод get_area(), 
который возвращает площадь круга (π * radius^2).
Алгоритм:
Создай класс Circle.
В методе __init__ сохрани радиус как атрибут объекта.
Определи метод get_area(), который вернет площадь (3.14 * self.radius ** 2).
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        print(f"{3.14 * self.radius ** 2}")


krug = Circle(4)
krug.get_area()
'''
Задача 11: Класс для студента
Напиши класс Student, который будет хранить имя (name) и курс (course). Добавь метод get_info(), 
который возвращает строку "Студент: [имя], Курс: [курс]".
Алгоритм:
Создай класс Student.
В методе __init__ сохрани имя и курс как атрибуты объекта.
Определи метод get_info(), который вернет форматированную строку.
'''
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def get_info(self):
        print(f"Студент: {self.name}, Курс: {self.course}")


student = Student("Пуци", 4)
student.get_info()
'''
Задача 12: Класс для телефона
Напиши класс Phone, который будет хранить номер (number). Добавь метод call(), который выводит строку "Звоню на [номер]".
Алгоритм:
Создай класс Phone.
В методе __init__ сохрани номер как атрибут объекта.
Определи метод call(), который выведет строку с номером.
'''
class Phone:
    def __init__(self, number):
        self.number = number
    def call(self):
        print(f"Звоню на {self.number}")


phone = Phone(89604914701)
phone.call()
'''
Задача 13: Класс для автомобиля
Напиши класс Car, который будет хранить марку (brand) и год выпуска (year). Добавь метод get_age(), 
который возвращает возраст автомобиля (разницу между текущим годом и year).
Алгоритм:
Создай класс Car.
В методе __init__ сохрани марку и год выпуска как атрибуты объекта.
Определи метод get_age(), который вернет 2023 - self.year.
'''
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def get_age(self):
        print(f"Автомобилю {self.brand} - {2023 - self.year} лет(года)")


car = Car("Daewoo Nexia", 2013)
car.get_age()
'''
Задача 14: Класс для счета
Напиши класс BankAccount, который будет хранить баланс (balance). Добавь метод deposit(amount), 
который увеличивает баланс на указанную сумму.
Алгоритм:
Создай класс BankAccount.
В методе __init__ установи начальный баланс (self.balance = 0).
Определи метод deposit(amount), который добавляет сумму к балансу.
'''
class BankAccount:
    def __init__(self):
        balance = 0
        self.balance = 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Баланс с учетом депозита = {self.balance}")


acc = BankAccount()
acc.deposit(100)
'''
Задача 15: Класс для песни
Напиши класс Song, который будет хранить название (title) и исполнителя (artist). 
Добавь метод play(), который выводит строку "Сейчас играет: [название] — [исполнитель]".
Алгоритм:
Создай класс Song.
В методе __init__ сохрани название и исполнителя как атрибуты объекта.
Определи метод play(), который выведет информацию о песне.
'''
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def play(self):
        print(f"Сейчас играет: {self.title} — {self.artist}")


song = Song("Звезда по имени солнце", "Виктор Цой")
song.play()
'''
Задача 16: Класс для треугольника
Напиши класс Triangle, который будет хранить стороны a, b, c. Добавь метод get_perimeter(), 
который возвращает периметр треугольника.
Алгоритм:
Создай класс Triangle.
В методе __init__ сохрани стороны как атрибуты объекта.
Определи метод get_perimeter(), который вернет self.a + self.b + self.c.
'''
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_perimeter(self):
        print(f"Периметр = {self.a + self.b + self.c}")


treug = Triangle(1, 4, 1)
treug.get_perimeter()
'''
Задача 17: Класс для фильма
Напиши класс Movie, который будет хранить название (title) и год выпуска (year). 
Добавь метод get_info(), который возвращает строку "Фильм: [название], Год: [год]".
Алгоритм:
Создай класс Movie.
В методе __init__ сохрани название и год выпуска как атрибуты объекта.
Определи метод get_info(), который вернет форматированную строку.
'''
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def get_info(self):
        print(f"Фильм: {self.title}, Год: {self.year}")


film = Movie("Чужой", 1979)
film.get_info()
'''
Задача 18: Класс для пользователя
Напиши класс User, который будет хранить имя (name) и возраст (age). 
Добавь метод is_adult(), который возвращает True, если возраст больше или равен 18, иначе False.
Алгоритм:
Создай класс User.
В методе __init__ сохрани имя и возраст как атрибуты объекта.
Определи метод is_adult(), который проверит возраст.
'''
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


user = User("Алексей", 37)
print(user.is_adult())
'''
Задача 19: Класс для книги (дополнительный метод)
Напиши класс Book, который будет хранить название (title) и автора (author). 
Добавь метод update_title(new_title), который изменяет название книги.
Алгоритм:
Создай класс Book.
В методе __init__ сохрани название и автора как атрибуты объекта.
Определи метод update_title(new_title), который обновит значение self.title.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def update_title(self, new_title):
        self.title = new_title
        print(f"Автор: {self.author}, название - {self.title}")


book = Book("Град обреченный", "Братья Стругацкие")
book.update_title("Пикник на обочине")
'''
Задача 20: Класс для банковской карты
Напиши класс CreditCard, который будет хранить номер карты (card_number) и баланс (balance). 
Добавь метод withdraw(amount), который уменьшает баланс на указанную сумму.
Алгоритм:
Создай класс CreditCard.
В методе __init__ сохрани номер карты и баланс как атрибуты объекта.
Определи метод withdraw(amount), который уменьшит баланс.
'''
class CrediCard:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            print("Нельзя с нять с карты сумму превышающую баланс!")
        else:
            self.balance = self.balance - amount
            print(f"Баланс карты = {self.balance}")


card = CrediCard(1234567, 5000)
card.withdraw(5100)
card.withdraw(700)
'''
Задача 21: Класс для магазина
Напиши класс Store, который будет хранить название магазина (name) и список товаров (items). 
Добавь метод add_item(item), который добавляет товар в список.
Алгоритм:
Создай класс Store.
В методе __init__ сохрани название и создай пустой список товаров (self.items = []).
Определи метод add_item(item), который добавит товар в список.
'''
class Store:
    def __init__(self, name):
        self.items = []
        self.name = name
    def add_item(self, item):
        self.items.append(item)
        print(f"Текущий список товаров: {self.items}")


store = Store("Магнит")
store.add_item("Яблочко")
store.add_item("Капустка")
'''
Задача 22: Класс для животного (дополнительный метод)
Напиши класс Animal, который будет хранить вид (species) и возраст (age). Добавь метод is_old(), 
который возвращает True, если возраст больше 10, иначе False.
Алгоритм:
Создай класс Animal.
В методе __init__ сохрани вид и возраст как атрибуты объекта.
Определи метод is_old(), который проверит возраст.
'''
class Animal:
    def __init__(self,species, age):
        self.species = species
        self.age = age
    def is_old(self):
        if self.age >= 10:
            return True
        else:
            return False


ape = Animal("ape", 11)
print(ape.is_old())
cat = Animal("cat", 2)
print(cat.is_old())
'''
Задача 23: Класс для кофемашины
Напиши класс CoffeeMachine, который будет хранить количество воды (water) и кофе (coffee). 
Добавь метод make_coffee(), который уменьшает количество воды и кофе на 10 единиц.
Алгоритм:
Создай класс CoffeeMachine.
В методе __init__ сохрани количество воды и кофе как атрибуты объекта.
Определи метод make_coffee(), который уменьшит ресурсы.
'''
class CoffeeMachine:
    def __init__(self, water, coffee):
        self.water = water
        self.coffee = coffee
    def make_coffee(self):
        if self.water < 10 and self.coffee < 10:
            print("Ресурсы для кофе  исчерпаны!")
        else:
            self.water -= 10
            self.coffee -= 10
            print("Наслаждайтесь кружечкой кофе!")


cup = CoffeeMachine(12, 14)
cup.make_coffee()
cup.make_coffee()