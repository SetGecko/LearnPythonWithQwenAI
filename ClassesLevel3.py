'''
Задача 1: Класс для автомобиля
Напиши класс Car, который хранит марку (brand), год выпуска (year), пробег (mileage) и
расход топлива (fuel_consumption). Добавь метод drive(distance),
который увеличивает пробег на указанное расстояние и рассчитывает расход топлива.
Также добавь метод is_old(), который проверяет, является ли автомобиль старым (>10 лет).
Алгоритм:
Создай класс Car.
В методе __init__ сохрани параметры brand, year, mileage и fuel_consumption.
Определи метод drive(distance), который:
Увеличивает пробег (mileage) на distance.
Рассчитывает расход топлива: (distance / 100) * fuel_consumption.
Определи метод is_old(), который проверяет возраст автомобиля.
'''
class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.fuel_consumption = 0
    def drive(self, distance):
        self.mileage += distance
        self.fuel_consumption = (distance / 100) * self.fuel_consumption
        return self.mileage, self.fuel_consumption
    def is_old(self):
        if self.year > 10:
            return True
        else:
            return False


c1 = Car("Daewoo Nexia", 2013, 33000)
print(c1.drive(200))
print(c1.is_old())
'''
Напиши класс BankAccount, который хранит имя владельца (owner), баланс (balance) и 
процентную ставку (interest_rate). Добавь метод withdraw(amount), который уменьшает баланс. 
Если сумма превышает баланс, добавь сообщение "Недостаточно средств!". 
Также добавь метод add_interest(), который начисляет проценты на баланс.
Алгоритм:
Создай класс BankAccount.
В методе __init__ сохрани параметры owner, balance и interest_rate.
Определи метод withdraw(amount), который проверяет сумму и уменьшает баланс.
Определи метод add_interest(), который увеличивает баланс на проценты:
balance += balance * (interest_rate / 100).
'''
class BankAccount:
    def __init__(self, owner, balance, interest_rate):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостаточно средств!"
        else:
            self.balance = self.balance - amount
            return f"Баланс карты = {self.balance}"
    def add_interest(self):
        if self.balance > 0:
            self.balance += self.balance * (self.interest_rate / 100)
            return f"Баланс после начисления процентов = {self.balance:.2f}"
        else:
            return "Проценты не начисляются на отрицательный баланс."


b1 = BankAccount("Алексей", 10000, 4)
print(b1.withdraw(20000))
print(b1.withdraw(3000))
print(b1.add_interest())
'''
Задача 3: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width), высоту (height) и цвет (color). 
Добавь метод scale(factor), который увеличивает размеры на указанный коэффициент. 
Также добавь метод get_area(), который возвращает площадь, и метод change_color(new_color), который меняет цвет.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width, height и color.
Определи метод scale(factor), который масштабирует размеры.
Определи метод get_area(), который вычисляет площадь.
Определи метод change_color(new_color), который обновляет цвет.
'''
class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    def scale(self, factor):
        if factor == 0 or factor < 0:
            return "Масштабирование невозможно равным 0 или менее его"
        else:
            self.width *= factor
            self.height *= factor
            return self.width, self.height
    def get_area(self):
        area = self.width * self.height
        return f"Площадь = {area}"
    def new_color(self,nc):
        self.color = nc
        return self.color


rc = Rectangle(5, 6, "red")
print(rc.scale(2))
print(rc.get_area())
print(rc.new_color("зеленый"))
'''
Задача 5: Класс для списка покупок
Напиши класс ShoppingList, который хранит название магазина (name) и список товаров (items). 
Добавь метод add_item(item), который добавляет товар. Также добавь метод remove_item(item), 
который удаляет товар, и метод total_price(prices), который считает общую стоимость товаров.
Алгоритм:
Создай класс ShoppingList.
В методе __init__ сохрани название магазина и создай пустой список товаров.
Определи метод add_item(item) для добавления товара.
Определи метод remove_item(item) для удаления товара.
Определи метод total_price(prices), который:
Принимает словарь цен (prices), где ключ — название товара, значение — цена.
Считает общую стоимость товаров из списка.
'''
class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        return self.items
    def remove_item(self, item):
        self.items.remove(item)
        return self.items
    def total_price(self, prices):
        total = 0
        for item in self.items:
            if item in prices:
                total += prices[item]
            else:
                print(f"Цена для товара '{item}' не указана.")
        return f"Общая стоимость товаров: {total} рублей"


shopping_list = ShoppingList("Магазин")
shopping_list.add_item("Хлеб")
shopping_list.add_item("Молоко")
shopping_list.add_item("Яблоки")
prices = {
    "Хлеб": 50,
    "Молоко": 80,
    "Яблоки": 60
}
print(shopping_list.total_price(prices))
'''
Задача 6: Класс для человека
Напиши класс Person, который хранит имя (name), возраст (age) и рост (height). 
Добавь метод celebrate_birthday(), который увеличивает возраст на 1. 
Также добавь метод can_drive(), который проверяет, может ли человек водить машину (возраст >=16), 
и метод bmi(weight), который вычисляет индекс массы тела.
Алгоритм:
Создай класс Person.
В методе __init__ сохрани параметры name, age и height.
Определи метод celebrate_birthday(), который увеличивает возраст.
Определи метод can_drive(), который проверяет возраст.
Определи метод bmi(weight), который:
Принимает вес (weight).
Рассчитывает BMI: weight / (height / 100) ** 2.
'''
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def celebrate_birthday(self):
        self.age += 1
        return self.age
    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False
    def bmi(self, weight):
        return f"BMI: {weight / (self.height / 100)}"


p1 = Person("Алексей", 37, 180)
print(p1.celebrate_birthday())
print(p1.can_drive())
print(p1.bmi(103))
'''
Задача 7: Класс для книги
Напиши класс Book, который хранит название (title), автора (author) и год выпуска (year). 
Добавь метод get_age(), который возвращает возраст книги. Также добавь метод update_year(new_year), 
который меняет год выпуска, и метод is_recent(), который проверяет, выпущена ли книга в последние 10 лет.
Алгоритм:
Создай класс Book.
В методе __init__ сохрани параметры title, author и year.
Определи метод get_age(), который вычисляет возраст.
Определи метод update_year(new_year), который обновляет год.
Определи метод is_recent(), который проверяет условие.
'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_age(self):
        return 2025 - self.year
    def update_year(self, new_year):
        self.year = new_year
        return self.year
    def is_recent(self):
        if self.year <= 10:
            return True
        else:
            return False


b1 = Book("Пикник на обочине", "Братья Стругацкие", 1979)
print(b1.get_age())
print(b1.update_year(1980))
print(b1.is_recent())
'''
Задача 8: Класс для телефона
Напиши класс Phone, который хранит номер (number) и список вызовов (calls). 
Добавь метод add_call(call), который добавляет новый вызов. 
Также добавь метод last_call(), который возвращает последний вызов, и метод call_duration(duration), 
который сохраняет длительность каждого вызова.
Алгоритм:
Создай класс Phone.
В методе __init__ сохрани параметр number и создай пустой список calls.
Определи метод add_call(call), который добавляет вызов.
Определи метод last_call(), который возвращает последний элемент списка.
Определи метод call_duration(duration), который:
Сохраняет длительность каждого вызова.
Добавляет её в список.
'''
class Phone:
    def __init__(self, number, calls):
        self.number = number
        self.calls = []
        self.call_durations = []
    def add_call(self, call):
        self.calls.append(call)
        return self.calls
    def last_call(self):
        return self.list[-1]
    def call_duration(self, duration):
        self.call_durations.append(duration)
        return f"Добавлена длительность вызова: {duration} секунд."
'''
Задача 9: Класс для города
Напиши класс City, который хранит название (name), население (population) и площадь (area). 
Добавь метод is_megacity(), который проверяет, является ли город мегаполисом (>10 млн). 
Также добавь метод density(), который вычисляет плотность населения.
Алгоритм:
Создай класс City.
В методе __init__ сохрани параметры name, population и area.
Определи метод is_megacity(), который проверяет население.
Определи метод density(), который:
Вычисляет плотность: population / area.
'''
class City:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    def is_meagacity(self):
        if self.population > 10000000:
            return True
        else:
            return False
    def density(self):
        return self.population / self.area


c1 = City("Краснодар", 11000000, 1300)
print(c1.is_meagacity())
print(c1.density())
'''
Задача 10: Класс для времени
Напиши класс Time, который хранит часы (hours) и минуты (minutes). 
Добавь метод add_time(other_time), который прибавляет другое время. 
Также добавь метод is_night(), который проверяет, 
является ли время ночью (между 22:00 и 6:00), и метод to_minutes(), который преобразует время в минуты.
Алгоритм:
Создай класс Time.
В методе __init__ сохрани параметры hours и minutes.
Определи метод add_time(other_time) для сложения времени.
Определи метод is_night(), который проверяет условие.
Определи метод to_minutes(), который:
Преобразует часы и минуты в общее количество минут: hours * 60 + minutes.
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
        return self.hours >= 22 or self.hours < 6
    def to_minutes(self):
        return self.hours * 60 + self.minutes
'''
Задача 11: Класс для кофемашины
Напиши класс CoffeeMachine, который хранит количество воды (water), кофе (coffee) и молока (milk). 
Добавь метод make_coffee(type), который делает чашку кофе определенного типа. 
Также добавь метод refill(), который пополняет все ресурсы.
Алгоритм:
Создай класс CoffeeMachine.
В методе __init__ сохрани параметры water, coffee и milk.
Определи метод make_coffee(type), который:
Для эспрессо: -10 воды и -5 кофе.
Для капучино: -10 воды, -5 кофе и -10 молока.
Определи метод refill(), который:
Пополняет все ресурсы до максимума.
'''
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def make_coffee(self, cof):
        if cof.lower() == "эспрессо":
            if self.coffee < 5 or self.water < 10:
                return "Недостаточно ресурсов!"
            else:
                self.coffee -= 5
                self.water -= 10
                return "Наслаждайтесь ароматным эспрессо"
        elif cof.lower() == "капучино":
            if self.coffee < 5 or self.water < 10 or self.milk < 10:
                return "Недостаточно ресурсов!"
            else:
                self.coffee -= 5
                self.water -= 10
                self.milk -= 10
                return "Наслаждайтесь ароматным капучино"
    def refill(self):
        self.coffee = 20
        self.water = 20
        self.milk = 20
        return "Кофемашина заправлена, время для кофе!"


c1 = CoffeeMachine(10, 1, 10)
print(c1.make_coffee("эспрессо"))
'''
Задача 12: Класс для студента
Напиши класс Student, который хранит имя (name), возраст (age) и список оценок (grades). 
Добавь метод average_grade(), который возвращает среднюю оценку. 
Также добавь метод add_grade(grade), который добавляет новую оценку.
Алгоритм:
Создай класс Student.
В методе __init__ сохрани параметры name, age и создай пустой список grades.
Определи метод add_grade(grade), который добавляет оценку.
Определи метод average_grade(), который:
Проверяет, что список оценок не пустой.
Вычисляет среднее значение: sum(grades) / len(grades).
'''
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.list = list(grades)
    def add_grade(self, grade):
        self.list.append(grade)
        return self.list
    def average_grade(self):
        sum = 0
        ave = 0
        for el in self.list:
            sum += el
        ave = sum / len(self.list)
        return ave


s1 = Student("Алексей", [5, 4, 3, 5, 5])
print(s1.average_grade())
print(s1.add_grade(4))
'''
Задача 13: Класс для магазина
Напиши класс Store, который хранит название (name) и список товаров (items). 
Добавь метод add_item(item), который добавляет товар. 
Также добавь метод remove_item(item), который удаляет товар, если он есть.
Алгоритм:
Создай класс Store.
В методе __init__ сохрани название и создай пустой список items.
Определи метод add_item(item), который добавляет товар.
Определи метод remove_item(item), который:
Проверяет наличие товара в списке.
Если товар есть, удаляет его.
Если товара нет, выводит сообщение "Товар отсутствует!".
'''
class Store:
    def __init__(self, name, items):
        self.list = list(items)
        self.name = name
    def add_item(self, item):
        self.list.append(item)
        return self.list
    def remove_item(self, item):
        if item in self.list:
            self.list.remove(item)
            return self.list
        else:
            return "Товар отсутствует!"


st1 = Store("Магнит", ["Яблок", "Петрушка", "Лук"])
print(st1.add_item("Тархун"))
print(st1.remove_item("Тархун"))
print(st1.remove_item("Лягушка"))
'''
Задача 14: Класс для банковской карты
Напиши класс CreditCard, который хранит номер карты (card_number), баланс (balance) и лимит (limit). 
Добавь метод withdraw(amount), который уменьшает баланс. Если сумма превышает баланс или лимит, 
добавь сообщение "Операция невозможна!". Также добавь метод set_limit(new_limit), который обновляет лимит.
Алгоритм:
Создай класс CreditCard.
В методе __init__ сохрани параметры card_number, balance и limit.
Определи метод withdraw(amount), который:
Проверяет, что amount <= balance и amount <= limit.
Если условия выполняются, уменьшает баланс.
Иначе выводит сообщение "Операция невозможна!".
Определи метод set_limit(new_limit), который обновляет лимит.
'''
class CreditCard:
    def __init__(self, card_number, balance, limit):
        self.balance = balance
        self.card_number = card_number
        self.limit = limit
    def withdraw(self, amount):
        if amount <= self.balance and amount <= self.limit:
            return "Операция невозможна!"
        else:
            self.balance -= amount
            return self.balance
    def set_limit(self, new_limit):
        self.limit = new_limit
        return self.limit


cr1 = CreditCard(123098, 10000, 500)
print(cr1.withdraw(600))
print(cr1.set_limit(400))
print(cr1.withdraw(300))