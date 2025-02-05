'''
Задача 1: Класс для автомобиля
Напиши класс Car, который хранит марку (brand), год выпуска (year) и пробег (mileage).
Добавь метод drive(distance), который увеличивает пробег на указанное расстояние.
Если пробег превышает 100,000 км, добавь метод is_old(), который возвращает True.
Алгоритм:
Создай класс Car.
В методе __init__ сохрани параметры brand, year и mileage.
Определи метод drive(distance), который увеличивает пробег.
Определи метод is_old(), который проверяет условие.
'''
class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage
    def drive(self, distance):
        self.mileage += distance
        return self.mileage
    def id_old(self):
        if self.mileage > 100000:
            return True
        else:
            return False


da = Car("Daewoo Nexia", 2013, 37000)
print(da.id_old())
da.drive(500000)
print(da.id_old())
'''
Задача 2: Класс для банковского счета
Напиши класс BankAccount, который хранит имя владельца (owner) и баланс (balance). 
Добавь метод withdraw(amount), который уменьшает баланс. 
Если сумма превышает баланс, добавь сообщение "Недостаточно средств!". 
Также добавь метод get_balance(), который возвращает текущий баланс.
Алгоритм:
Создай класс BankAccount.
В методе __init__ сохрани параметры owner и balance.
Определи метод withdraw(amount) для списания средств.
Определи метод get_balance() для получения баланса.
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Недостаточно средств!"
    def get_balance(self):
        return f"Баланс = {self.balance}"


bank = BankAccount("Алексей", 5000)
bank.withdraw(300)
print(bank.get_balance())
print(bank.withdraw(6000))
'''
Задача 3: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width) и высоту (height). 
Добавь метод scale(factor), который увеличивает размеры на указанный коэффициент. 
Также добавь метод get_area(), который возвращает площадь.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width и height.
Определи метод scale(factor) для масштабирования.
Определи метод get_area() для вычисления площади.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def scale(self, factor):
        if factor == 0 or factor < 0:
            return "Масштабирование невозможно равным 0 или менее его"
        else:
            self.width *= factor
            self.height *= factor
    def get_area(self):
        area = self.width * self.height
        return f"Площадь = {area}"


rect = Rectangle(4, 3)
print(rect.get_area())
'''
Задача 4: Класс для точки
Напиши класс Point, который хранит координаты x и y. 
Добавь метод distance_to(other_point), который вычисляет расстояние до другой точки. 
Также добавь метод move(dx, dy), который перемещает точку.
Алгоритм:
Создай класс Point.
В методе __init__ сохрани координаты x и y.
Определи метод distance_to(other_point) для вычисления расстояния.
Определи метод move(dx, dy) для перемещения точки.
'''
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
'''
Задача 5: Класс для списка покупок
Напиши класс ShoppingList, который хранит название магазина (name) и список товаров (items). 
Добавь метод add_item(item), который добавляет товар. 
Также добавь метод remove_item(item), который удаляет товар.
Алгоритм:
Создай класс ShoppingList.
В методе __init__ сохрани название и создай пустой список товаров.
Определи метод add_item(item) для добавления товара.
Определи метод remove_item(item) для удаления товара.
'''
class ShoppingList:
    def __init__(self, name, items):
        self.name = name
        self.list = list(items)
    def add_item(self, item):
        self.list.append(item)
        return self.list
    def remove_item(self, item):
        self.list.remove(item)
        return self.list


sl = ShoppingList("Магнит", ["Яблоки", "Тархун"])
print(sl.add_item("Чабрец"))
print(sl.remove_item("Чабрец"))
'''
Задача 6: Класс для человека
Напиши класс Person, который хранит имя (name) и возраст (age). 
Добавь метод celebrate_birthday(), который увеличивает возраст на 1. 
Также добавь метод can_drive(), который проверяет, может ли человек водить машину (возраст >=16).
Алгоритм:
Создай класс Person.
В методе __init__ сохрани параметры name и age.
Определи метод celebrate_birthday(), который увеличивает возраст.
Определи метод can_drive(), который проверяет возраст.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def celebrate_birthday(self):
        self.age += 1
        return self.age
    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False


pers = Person("Алексей", 15)
print(pers.can_drive())
print(pers.celebrate_birthday())
print(pers.can_drive())
'''
Задача 7: Класс для книги
Напиши класс Book, который хранит название (title), автора (author) и год выпуска (year). 
Добавь метод get_age(), который возвращает возраст книги. 
Также добавь метод is_recent(), который проверяет, выпущена ли книга в последние 10 лет.
Алгоритм:
Создай класс Book.
В методе __init__ сохрани параметры title, author и year.
Определи метод get_age(), который вычисляет возраст.
Определи метод is_recent(), который проверяет год выпуска.
'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_age(self):
        age = 2025 - self.year
        return f"Возраст книги = {age}"
    def is_recent(self):
        age = 2025 - self.year
        if age <= 10:
            return True
        else:
            return False


b1 = Book("Пикник на обочине", "Братья Стругацкие", 1979)
print(b1.get_age())
print(b1.is_recent())
'''
Задача 8: Класс для телефона
Напиши класс Phone, который хранит номер (number) и список вызовов (calls). 
Добавь метод add_call(call), который добавляет новый вызов. 
Также добавь метод last_call(), который возвращает последний вызов.
Алгоритм:
Создай класс Phone.
В методе __init__ сохрани параметр number и создай пустой список calls.
Определи метод add_call(call) для добавления вызова.
Определи метод last_call(), который возвращает последний элемент списка.
'''
class Phone:
    def __init__(self, number, calls):
        self.number = number
        self.list = list(calls)
    def add_call(self, call):
        self.list.append(call)
        return self.list
    def last_call(self):
        return self.list[-1]


ph = Phone(89604914701, [12, 14, 44])
print(ph.add_call(73))
print(ph.last_call())
'''
Задача 9: Класс для города
Напиши класс City, который хранит название (name) и население (population). 
Добавь метод is_megacity(), который проверяет, является ли город мегаполисом (>10 млн). 
Также добавь метод update_population(change), который изменяет население.
Алгоритм:
Создай класс City.
В методе __init__ сохрани параметры name и population.
Определи метод is_megacity(), который проверяет население.
Определи метод update_population(change), который изменяет население.
'''
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def is_megacity(self):
        if self.population >= 10000000:
            return True
        else:
            return False
    def update_population(self, change):
        self.population += change
        return self.population


k1 = City("Краснодар", 1200000)
print(k1.is_megacity())
print(k1.update_population(30000000))
print(k1.is_megacity())
'''
Задача 10: Класс для времени
Напиши класс Time, который хранит часы (hours) и минуты (minutes). 
Добавь метод add_time(other_time), который прибавляет другое время. 
Также добавь метод is_night(), который проверяет, является ли время ночью (между 22:00 и 6:00).
Алгоритм:
Создай класс Time.
В методе __init__ сохрани параметры hours и minutes.
Определи метод add_time(other_time) для сложения времени.
Определи метод is_night(), который проверяет условие.
'''
class Time:
    def __init__(self, hours, minutes):
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
        self.hours = hours
        self.minutes = minutes
    def add_time(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        total_hours = self.hours + other_time.hours + total_minutes // 60
        total_hours = total_hours % 24
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)
    def is_night(self):
        return (self.hours >= 22 or self.hours < 6)


t1 = Time(10, 15)
t2 = Time(12, 11)
print(t1.add_time(t2))
print(t1.is_night())
'''
Задача 11: Класс для кофемашины
Напиши класс CoffeeMachine, который хранит количество воды (water) и кофе (coffee). 
Добавь метод make_coffee(count), который делает несколько чашек кофе. 
Если ресурсов не хватает, добавь сообщение "Ресурсы исчерпаны!".
Алгоритм:
Создай класс CoffeeMachine.
В методе __init__ сохрани параметры water и coffee.
Определи метод make_coffee(count) для изготовления кофе.
Проверь ресурсы перед изготовлением.
'''
class CoffeeMachine:
    def __init__(self, water, coffee):
        self.water = water
        self.coffee = coffee
    def make_coffee(self, count):
        if self.water < count*10 and self.coffee < count*10:
            return "Ресурсы исчерпаны!"
        else:
            self.water -= count*10
            self.coffee -= count*10
            return "Наслаждайтесь кофе!"


cf = CoffeeMachine(11, 17)
print(cf.make_coffee(2))
'''
Задача 12: Класс для пользователя
Напиши класс User, который хранит имя (name) и email. 
Добавь метод update_email(new_email), который обновляет email. 
Также добавь метод validate_email(), который проверяет корректность email.
Алгоритм:
Создай класс User.
В методе __init__ сохрани параметры name и email.
Определи метод update_email(new_email) для изменения email.
Определи метод validate_email(), который проверяет наличие символа "@".
'''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def update_email(self, new_email):
        self.email = new_email
        return self.email
    def validate_email(self):
        if "@" in self.email:
            return True
        else:
            return False


us1 = User("Алексей", "setgecko@gmail.com")
print(us1.update_email("bubu.mail"))
print(us1.validate_email())
'''
Задача 13: Класс для треугольника
Напиши класс Triangle, который хранит стороны a, b, c. 
Добавь метод is_valid(), который проверяет, существует ли треугольник. 
Также добавь метод get_type(), который определяет тип треугольника.
Алгоритм:
Создай класс Triangle.
В методе __init__ сохрани параметры a, b, c.
Определи метод is_valid(), который проверяет сумму сторон.
Определи метод get_type(), который возвращает тип треугольника.
'''
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False
    def get_type(self):
        if self.a == self.b == self.c:
            return "Равносторонний"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Равнобедренный"
        else:
            return "Разносторонний"


tr1 = Triangle(1, 1, 2)
print(tr1.is_valid())
print(tr1.get_type())
'''
Задача 14: Класс для фильма
Напиши класс Movie, который хранит название (title), год выпуска (year) и продолжительность (duration). 
Добавь метод is_long(), который проверяет, является ли фильм длинным (>120 минут). 
Также добавь метод update_year(new_year), который меняет год выпуска.
Алгоритм:
Создай класс Movie.
В методе __init__ сохрани параметры title, year и duration.
Определи метод is_long(), который проверяет продолжительность.
Определи метод update_year(new_year), который обновляет год.
'''
class Movie:
    def __init__(self, title, year, duration):
        self.title = title
        self.year = year
        self.duration = duration
    def is_long(self):
        if self.duration > 120:
            return True
        else:
            return False
    def update_year(self,new_year):
        self.year = new_year
        return self.year


m1 = Movie("Чужой", 1979, 130)
print(m1.is_long())
print(m1.update_year(1980))
'''
Задача 15: Класс для круга
Напиши класс Circle, который хранит радиус (radius). 
Добавь метод get_area(), который возвращает площадь. 
Также добавь метод is_small(), который проверяет, является ли площадь маленькой (<50).
Алгоритм:
Создай класс Circle.
В методе __init__ сохрани параметр radius.
Определи метод get_area(), который вычисляет площадь.
Определи метод is_small(), который проверяет условие.
'''
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = pi * radius ** 2
    def get_area(self):
        return self.area
    def is_small(self):
        if self.area < 50:
            return True
        else:
            return False


c1 = Circle(90)
print(c1.get_area())
print(c1.is_small())
'''
Задача 16: Класс для банковской карты
Напиши класс CreditCard, который хранит номер карты (card_number) и баланс (balance). 
Добавь метод withdraw(amount), который уменьшает баланс. 
Если сумма превышает баланс, добавь сообщение "Недостаточно средств!". 
Также добавь метод transaction_history(), который сохраняет историю операций.
Алгоритм:
Создай класс CreditCard.
В методе __init__ сохрани параметры card_number и balance.
Определи метод withdraw(amount) для списания средств.
Создай атрибут history для хранения истории операций.
'''
class CreditCard:
    def __init__(self, card_number, balance):
        self.balance = balance
        self.card_number = card_number
        self.history = []
    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостаточно средств!"
        else:
            self.balance = self.balance - amount
            return f"Баланс карты = {self.balance}"
            self.history.append(self.balance)
    def transaction_history(self):
        if not self.history:
            return
        return self.history


c1 = CreditCard(123098, 5000)
print(c1.withdraw(400))
print(c1.withdraw(700))
print(c1.transaction_history())
print(c1.withdraw(10000))
'''
Задача 17: Класс для студента
Напиши класс Student, который хранит имя (name) и список оценок (grades). 
Добавь метод average_grade(), который возвращает среднюю оценку. 
Также добавь метод best_grade(), который возвращает максимальную оценку.
Алгоритм:
Создай класс Student.
В методе __init__ сохрани параметр name и создай пустой список grades.
Определи метод average_grade(), который вычисляет среднее значение.
Определи метод best_grade(), который находит максимальную оценку.
'''
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.list = list(grades)
    def average_grade(self):
        sum = 0
        ave = 0
        for el in self.list:
            sum += el
        ave = sum / len(self.list)
        return ave
    def best_grade(self):
        return max(self.list)


st = Student("Алексей", [5, 5, 4, 3, 5])
print(st.average_grade())
print(st.best_grade())
'''
Задача 18: Класс для животного
Напиши класс Animal, который хранит вид (species) и возраст (age). 
Добавь метод can_speak(), который проверяет, может ли животное говорить (возраст >1). 
Также добавь метод update_age(years), который изменяет возраст.
Алгоритм:
Создай класс Animal.
В методе __init__ сохрани параметры species и age.
Определи метод can_speak(), который проверяет возраст.
Определи метод update_age(years), который обновляет возраст.
'''
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    def can_speak(self):
        if self.age > 1:
            return True
        else:
            return False
    def update_age(self, new_age):
        self.age = new_age
        return self.age


an = Animal("Cat", 2)
print(an.can_speak())
print(an.update_age(3))
'''
Задача 19: Класс для машины
Напиши класс Car, который хранит марку (brand), год выпуска (year) и пробег (mileage). 
Добавь метод fuel_consumption(liters), который обновляет расход топлива. 
Также добавь метод get_fuel_efficiency(), который вычисляет эффективность использования топлива.
Алгоритм:
Создай класс Car.
В методе __init__ сохрани параметры brand, year и mileage.
Определи метод fuel_consumption(liters) для обновления расхода.
Определи метод get_fuel_efficiency(), который вычисляет эффективность.
'''
class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = 0  # Начальный расход топлива

    def update_fuel_consumption(self, liters):  # Переименовал метод
        self.fuel_consumption += liters

    def get_fuel_efficiency(self):
        if self.fuel_consumption == 0:
            return "Недостаточно данных для расчета эффективности."
        efficiency = self.mileage / self.fuel_consumption
        return f"Эффективность использования топлива: {efficiency:.2f} км/л"

car = Car("Daewoo Nexia", 2013, 33200)
car.update_fuel_consumption(100)
print(car.get_fuel_efficiency())
'''
Задача 20: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width) и высоту (height). 
Добавь метод rotate(), который меняет ширину и высоту местами. 
Также добавь метод get_diagonal(), который возвращает диагональ.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width и height.
Определи метод rotate(), который меняет размеры местами.
Определи метод get_diagonal(), который вычисляет диагональ через теорему Пифагора.
'''
from math import sqrt
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def rotate(self):
        kva_w = self.width
        self.width = self.height
        self.height = kva_w
        return self.width, self.height
    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)


r1 = Rectangle(4, 3)
print(r1.rotate())
print(r1.get_diagonal())