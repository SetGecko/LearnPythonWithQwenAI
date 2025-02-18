'''
Что такое композиция?
Композиция — это концепция объектно-ориентированного программирования (ООП),
при которой один класс содержит объекты другого класса как свои атрибуты.
Это позволяет создавать более сложные структуры данных, комбинируя объекты разных классов.

Проще говоря, композиция — это когда один объект "состоит" из других объектов. Например:

Автомобиль состоит из двигателя, колес, кузова.
Компьютер состоит из процессора, оперативной памяти, жесткого диска.


Основные моменты композиции
Объекты как атрибуты:
Один класс может содержать объекты других классов как свои атрибуты.
Делегирование:
Главный класс может "делегировать" выполнение задач своим компонентам.
Например, класс Car вызывает метод start() у объекта Engine.
Гибкость:
Можно легко менять или добавлять компоненты. Например, вместо Engine подключить ElectricEngine.


Зачем нужна композиция?
Модульность:
Каждый компонент системы можно описать отдельным классом, что делает код более организованным и понятным.
Расширяемость:
Если нужно добавить новый компонент, можно просто создать соответствующий класс и
использовать его в существующей системе.
Гибкость:
Объекты могут состоять из разных компонентов, что позволяет создавать уникальные конфигурации.


Когда использовать композицию?
Если объект состоит из других объектов:
Например, компьютер состоит из процессора, памяти и диска. Каждую часть можно описать отдельным классом.
Если нужно разделить ответственность:
Разные классы отвечают за разные функции, что делает код более чистым и понятным.
Если нужно создать гибкую систему:
Можно легко заменять или модифицировать компоненты. Например, вместо обычного двигателя подключить электродвигатель.


Объект "Автомобиль":
Автомобиль может содержать двигатель, колеса и другие компоненты. Каждый компонент — это отдельный класс.

# Класс Engine (двигатель)
class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return f"Двигатель мощностью {self.power} л.с. запущен."

# Класс Wheel (колесо)
class Wheel:
    def __init__(self, size):
        self.size = size

    def info(self):
        return f"Колесо размером {self.size} дюймов."

# Класс Car (автомобиль)
class Car:
    def __init__(self, brand, engine_power, wheel_size):
        self.brand = brand
        # Создаем объекты компонентов внутри класса Car
        self.engine = Engine(engine_power)  # Двигатель
        self.wheel = Wheel(wheel_size)      # Колесо

    def get_info(self):
        return (
            f"Автомобиль: {self.brand}\n"
            f"{self.engine.start()}\n"  # Используем метод класса Engine
            f"{self.wheel.info()}"     # Используем метод класса Wheel
        )

# Создаем объект автомобиля
car = Car("Daewoo Nexia", 90, 14)
print(car.get_info())
'''

'''
Задача 1: Автомобиль
Алгоритм:
Создай класс Engine, который хранит мощность (power) двигателя.
Определи метод start(), который возвращает строку "Двигатель мощностью [power] л.с. запущен".
Создай класс Car, который хранит марку (brand) и объект класса Engine.
В методе __init__ создай объект класса Engine и сохрани его как атрибут (self.engine).
Определи метод get_info(), который:
Вызывает метод start() у объекта self.engine.
Возвращает строку "Автомобиль: [brand], Двигатель: [power] л.с.".
'''
class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        return f"Двигатель мощностью {self.power} л.с. запущен"

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)
    def get_info(self):
        return (
            f"Автомобиль: {self.brand}\n"
            f"{self.engine.start()}\n"
        )

car = Car("Daewoo Nexia", 87)
print(car.get_info())
'''
Задача 2: Компьютер
Алгоритм:
Создай класс Processor, который хранит количество ядер (cores).
Определи метод info(), который возвращает строку "Процессор с [cores] ядрами".
Создай класс Computer, который хранит название (name) и объект класса Processor.
В методе __init__ создай объект класса Processor и сохрани его как атрибут (self.processor).
Определи метод get_info(), который:
Вызывает метод info() у объекта self.processor.
Возвращает строку "Компьютер: [name], Процессор: [cores] ядра".
'''
class Processor:
    def __init__(self, cores):
        self.cores = cores

    def info(self):
        return  f"Процессор с {self.cores} ядрами"

class Computer:
    def __init__(self, name, cores):
        self.name = name
        self.processor = Processor(cores)

    def info(self):
        return (
            f"Компьютер: {self.name}\n"
            f"{self.processor.info()}\n"
        )

pc = Computer("iMac", 16)
print(pc.info())
'''
Задача 3: Человек
Алгоритм:
Создай класс Address, который хранит город (city) и улицу (street).
Определи метод get_address(), который возвращает строку "Город: [city], Улица: [street]".
Создай класс Person, который хранит имя (name) и объект класса Address.
В методе __init__ создай объект класса Address и сохрани его как атрибут (self.address).
Определи метод get_info(), который:
Вызывает метод get_address() у объекта self.address.
Возвращает строку "Имя: [name], Адрес: [city], [street]".
'''
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def get_address(self):
        return f"Город: {self.city}, Улица: {self.street}"

class Person:
    def __init__(self, name, city, street):
        self.name = name
        self.address = Address(city, street)

    def get_address(self):
        return (
            f"Имя: {self.name}\n"
            f"{self.address.get_address()}\n"
        )

pers = Person("Алексей", "Краснодар", "Рылеева")
print(pers.get_address())
'''
Задача 4: Фильм
Алгоритм:
Создай класс Director, который хранит имя режиссера (name).
Определи метод get_name(), который возвращает строку "Режиссер: [name]".
Создай класс Film, который хранит название (title) и объект класса Director.
В методе __init__ создай объект класса Director и сохрани его как атрибут (self.director).
Определи метод get_info(), который:
Вызывает метод get_name() у объекта self.director.
Возвращает строку "Фильм: [title], Режиссер: [name]".
'''
class Director:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Режиссер: {self.name}"

class Film:
    def __init__(self, title, name):
        self.title = title
        self.name = Director(name)

    def get_info(self):
        return (
            f"Фильм: {self.title}, {self.name.get_name()}"
        )

ff = Film("Чужой", "Риддли Скотт")
print(ff.get_info())
'''
Задача 5: Книга
Алгоритм:
Создай класс Author, который хранит имя автора (name).
Определи метод get_name(), который возвращает строку "Автор: [name]".
Создай класс Book, который хранит название (title) и объект класса Author.
В методе __init__ создай объект класса Author и сохрани его как атрибут (self.author).
Определи метод get_info(), который:
Вызывает метод get_name() у объекта self.author.
Возвращает строку "Книга: [title], Автор: [name]".
'''
class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Автор: {self.name}"

class Book:
    def __init__(self, title, name):
        self.title = title
        self.name = Author(name)

    def get_info(self):
        return (
            f"Книга: {self.title}, {self.name.get_name()}"
        )

bb = Book("Пикник у обочины", "Братья Стругацкие")
print(bb.get_info())
'''
Задача 6: Город
Алгоритм:
Создай класс Location, который хранит широту (latitude) и долготу (longitude).
Определи метод get_location(), который возвращает строку "Координаты: [latitude], [longitude]".
Создай класс City, который хранит название (name) и объект класса Location.
В методе __init__ создай объект класса Location и сохрани его как атрибут (self.location).
Определи метод get_info(), который:
Вызывает метод get_location() у объекта self.location.
Возвращает строку "Город: [name], Координаты: [latitude], [longitude]".
'''
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_location(self):
        return f"Координаты: {self.latitude}, {self.longitude}"

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = Location(latitude, longitude)

    def get_info(self):
        return (
            f"Город: {self.name}, {self.latitude.get_location()}"
        )

cc = City("Краснодар", 400, 599)
print(cc.get_info())
'''
Задача 7: Банковский счет
Алгоритм:
Создай класс Balance, который хранит текущий баланс (balance).
Определи метод withdraw(amount), который уменьшает баланс на указанную сумму.
Определи метод get_balance(), который возвращает текущий баланс.
Создай класс BankAccount, который хранит владельца (owner) и объект класса Balance.
В методе __init__ создай объект класса Balance и сохрани его как атрибут (self.balance).
Определи метод withdraw_money(amount), который:
Вызывает метод withdraw(amount) у объекта self.balance.
Возвращает результат операции.
Определи метод get_balance_info(), который вызывает метод get_balance() у объекта self.balance.
'''
class Balance:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Текущй баланс = {self.balance}"
        else:
            return "Недостаточно средств"

    def get_balance(self):
        return f"Текущий баланс = {self.balance}"

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = Balance(balance)

    def withdraw_money(self, amount):
        return f"{self.balance.withdraw(amount)}"

    def get_balance_info(self):
        return f"{self.balance.get_balance()}"

zz = BankAccount("Алексей", 9000)
print(zz.get_balance_info())
print(zz.withdraw_money(3000))
'''
Задача 8: Телефон
Алгоритм:
Создай класс Battery, который хранит уровень заряда (charge).
Определи метод use_battery(usage), который уменьшает заряд на указанное значение.
Определи метод get_charge(), который возвращает текущий заряд.
Создай класс Phone, который хранит номер (number) и объект класса Battery.
В методе __init__ создай объект класса Battery и сохрани его как атрибут (self.battery).
Определи метод make_call(duration), который:
Вызывает метод use_battery(duration) у объекта self.battery.
Выводит сообщение "Звонок продолжительностью [duration] минут".
Определи метод check_battery(), который вызывает метод get_charge() у объекта self.battery.
'''
class Battery:
    def __init__(self, charge):
        self.charge = charge

    def use_battery(self, usage):
        if self.charge >= usage:
            self.charge -= usage
            return True
        else:
            return False

    def get_charge(self):
        return f"Текущий заряд = {self.charge}"

class Phone:
    def __init__(self, number, charge):
        self.number = number
        self.charge = Battery(charge)

    def check_battery(self):
        return f"{self.charge.get_charge()}"

    def make_call(self, duration):
        if self.charge.use_battery(duration) == True:
            return f"Звонок продолжительностью {duration} минут"
        else:
            return "Нельзя!"

zz = Phone(8800, 100)
print(zz.check_battery())
print(zz.make_call(200))
'''
Задача 9: Машина времени
Алгоритм:
Создай класс TimeMachineControl, который хранит год назначения (year).
Определи метод set_year(new_year), который изменяет год назначения.
Определи метод get_year(), который возвращает текущий год назначения.
Создай класс TimeMachine, который хранит название (name) и объект класса TimeMachineControl.
В методе __init__ создай объект класса TimeMachineControl и сохрани его как атрибут (self.control).
Определи метод travel_to_year(), который вызывает метод set_year() у объекта self.control.
Определи метод get_travel_info(), который вызывает метод get_year() у объекта self.control.
'''
class TimeMachineControl:
    def __init__(self, year):
        self.year = year

    def set_year(self, new_year):
        if self.year <= 0:
            return False
        else:
            self.year = new_year
            return self.year

    def get_year(self):
        return self.year

class TimeMachine:
    def __init__(self, name, year):
        self.name = name
        self.control = TimeMachineControl(year)

    def travel_to_year(self, year):
        return f"{self.control.set_year(year)}"

    def get_travel_info(self):
        return f"{self.control.get_year()}"

mm = TimeMachine("Алексей", 1900)
print(mm.travel_to_year(1700))
print(mm.get_travel_info())
'''
Задача 10: Магазин
Алгоритм:
Создай класс Product, который хранит название товара (name) и цену (price).
Определи метод get_info(), который возвращает строку "Товар: [name], Цена: [price]".

Создай класс Store, который хранит название магазина (name) и список товаров (products).
В методе __init__ создай пустой список товаров (self.products = []).
Определи метод add_product(name, price), который:
Создает объект класса Product и добавляет его в список self.products.

Определи метод get_products_info(), который:
Перебирает все объекты в списке self.products.
Вызывает метод get_info() у каждого объекта и выводит результат.
'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Товар: {self.name}, Цена: {self.price}"

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def get_products_info(self):
        if not self.products:
            print("В магазине нет товаров.")
            return

        for product in self.products:
            print(product.get_info())

store = Store("Магнит")

store.add_product("Хлеб", 50)
store.add_product("Молоко", 80)
store.add_product("Яблоки", 60)
store.get_products_info()