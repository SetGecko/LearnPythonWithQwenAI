'''
инкапсуляции — это следующая важная концепция
 объектно-ориентированного программирования (ООП). Инкапсуляция позволяет ограничить доступ к атрибутам и методам
 класса, чтобы защитить данные от случайного изменения или внешнего вмешательства.

Что такое инкапсуляция?
Инкапсуляция — это механизм, при котором ты можешь скрыть внутренние детали класса и предоставить ограниченный доступ
 к его атрибутам и методам. Это делается с помощью специальных модификаторов доступа:

Общедоступные атрибуты (public):
Атрибуты, которые можно свободно читать и изменять извне класса.
Пример: self.name, self.age.
Защищенные атрибуты (protected):
Атрибуты, которые не должны быть доступны напрямую, но могут использоваться внутри класса или дочерних классов.
Обозначаются символом _ перед названием (например, self._salary).
Приватные атрибуты (private):
Атрибуты, которые полностью скрыты от внешнего мира и доступны только внутри самого класса.
Обозначаются двумя символами __ перед названием (например, self.__password).

Зачем нужна инкапсуляция?
Защита данных:
Инкапсуляция помогает предотвратить несанкционированное изменение важных данных.
Например, баланс банковского счета должен изменяться только через специальные методы, а не напрямую.
Контроль доступа:
Ты можешь контролировать, каким образом данные будут читаться или изменяться, используя геттеры и сеттеры.
Модульность кода:
Инкапсуляция делает код более организованным и понятным, так как ты явно указываешь,
какие атрибуты доступны для использования, а какие нет.

Как работает инкапсуляция в Python?
1. Общедоступные атрибуты:
class Person:
    def __init__(self, name, age):
        self.name = name  # Общедоступный атрибут
        self.age = age    # Общедоступный атрибут

person = Person("Алексей", 37)
print(person.name)  # Можно получить доступ напрямую

2. Защищенные атрибуты:
class Person:
    def __init__(self, name, salary):
        self.name = name          # Общедоступный атрибут
        self._salary = salary     # Защищенный атрибут

person = Person("Алексей", 50000)
print(person.name)       # Вывод: Алексей
# print(person._salary)  # Можно получить доступ, но это не рекомендуется

3. Приватные атрибуты:
class Person:
    def __init__(self, name, password):
        self.name = name             # Общедоступный атрибут
        self.__password = password   # Приватный атрибут

    def get_password(self):  # Геттер для приватного атрибута
        return self.__password

    def set_password(self, new_password):  # Сеттер для приватного атрибута
        self.__password = new_password

person = Person("Алексей", "qwerty")
# print(person.__password)  # Ошибка: приватный атрибут недоступен извне
print(person.get_password())  # Вывод: qwerty
person.set_password("12345")
print(person.get_password())  # Вывод: 12345

Где обычно используется инкапсуляция?
В банковских системах:
Баланс счета или пароль клиента могут быть приватными атрибутами, чтобы их нельзя было изменить напрямую.
В играх:
Здоровье персонажа или количество очков может быть защищенным атрибутом, доступным только через специальные методы.
В программах управления:
Конфиденциальные данные, такие как логины, пароли или настройки, часто хранятся как приватные атрибуты.

Геттеры и Сеттеры
Геттеры и сеттеры — это специальные методы, которые позволяют безопасно получать (get) и устанавливать
(set) значения приватных атрибутов.

class User:
    def __init__(self, name, age):
        self.__name = name  # Приватный атрибут
        self.__age = age    # Приватный атрибут

    def get_name(self):  # Геттер для имени
        return self.__name

    def set_name(self, new_name):  # Сеттер для имени
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            raise ValueError("Имя должно быть строкой и не пустым!")

    def get_age(self):  # Геттер для возраста
        return self.__age

    def set_age(self, new_age):  # Сеттер для возраста
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("Возраст должен быть целым числом и больше или равен 0.")

user = User("Алексей", 37)
print(user.get_name())  # Вывод: Алексей
user.set_name("Иван")   # Изменяем имя через сеттер
print(user.get_name())  # Вывод: Иван

print(user.get_age())   # Вывод: 37
user.set_age(40)       # Изменяем возраст через сеттер
print(user.get_age())   # Вывод: 40
'''

'''
===========Задачи с защищенными атрибутами===========
'''

'''
Задача 1: Класс для пользователя
Напиши класс User, который хранит имя (_name) и возраст (_age).
Добавь метод get_info(), который возвращает строку "Имя: [имя], Возраст: [возраст]".

Алгоритм:

Создай класс User.
В методе __init__ сохрани параметры _name и _age как защищенные атрибуты .
Определи метод get_info(), который:
Использует защищенные атрибуты _name и _age для формирования строки.
Убедись, что напрямую извне класса нельзя изменить _name или _age.
'''
# class User:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def get_info(self):
#         return f"Пользователь - {self._name}, Возраст - {self._age}"
#
#
# u1 = User("Алексей", 37)
# print(u1.get_info())
'''
Задача 2: Класс для банковского счета
Напиши класс BankAccount, который хранит баланс (_balance).
Добавь методы deposit(amount) и withdraw(amount), которые изменяют баланс.

Алгоритм:

Создай класс BankAccount.
В методе __init__ сохрани параметр _balance как защищенный атрибут .
Определи метод deposit(amount), который:
Проверяет, что amount > 0.
Прибавляет сумму к балансу.
Определи метод withdraw(amount), который:
Проверяет, что amount <= _balance.
Вычитает сумму из баланса.
Убедись, что баланс доступен только через методы.
'''
# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance
#     def deposit(self, amount):
#         self._balance += amount
#         return self._balance
#     def withdraw(self, amount):
#         if self._balance < amount:
#             return "Недостаточно средств!"
#         else:
#             self._balance -= amount
#             return self._balance
#
#
# ba = BankAccount(1000)
# print(ba.deposit(200))
# print(ba.withdraw(1300))
# print(ba.withdraw(800))
'''
Задача 3: Класс для книги
Напиши класс Book, который хранит название (_title) и год выпуска (_year).
Добавь метод update_year(new_year), который обновляет год выпуска.

Алгоритм:

Создай класс Book.
В методе __init__ сохрани параметры _title и _year как защищенные атрибуты .
Определи метод update_year(new_year), который:
Проверяет, что new_year > _year.
Обновляет значение _year.
Убедись, что доступ к _title и _year возможен только через методы.
'''
# class Book:
#     def __init__(self, title, year):
#         self._title = title
#         self._year = year
#     def update_year(self, new_year):
#         self._year = new_year
#         return self._year
#
#
# b1 = Book("Пикник на обочине", 1979)
# print(b1.update_year(1980))
'''
Задача 4: Класс для автомобиля
Напиши класс Car, который хранит пробег (_mileage) и марку (brand).
Добавь метод drive(distance), который увеличивает пробег.

Алгоритм:

Создай класс Car.
В методе __init__ сохрани параметры _mileage (защищенный атрибут) и brand (общедоступный).
Определи метод drive(distance), который:
Проверяет, что distance > 0.
Увеличивает _mileage на указанное расстояние.
Убедись, что пробег доступен только через методы.
'''
# class Car:
#     def __init__(self, mileage, brand):
#         self._mileage = mileage
#         self.brand = brand
#     def drive(self, distance):
#         if distance > 0:
#             self._mileage += distance
#             return self._mileage
#         else:
#             return "Пробег не может быть равным 0"
#
#
# c1 = Car(1000, "Daewoo Nexia")
# print(c1.drive(0))
# print(c1.drive(300))
'''
Задача 5: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (_width) и высоту (_height).
Добавь метод scale(factor), который увеличивает размеры.

Алгоритм:

Создай класс Rectangle.
В методе __init__ сохрани параметры _width и _height как защищенные атрибуты .
Определи метод scale(factor), который:
Проверяет, что factor > 0.
Умножает _width и _height на коэффициент.
Убедись, что размеры доступны только через методы.
'''
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#     def scale(self, factor):
#         if factor <= 0:
#             return "Скалирование невозможно"
#         else:
#             self._width *= factor
#             self._height *= factor
#             return self._width, self._height
#
#
# r1 = Rectangle(4, 2)
# print(r1.scale(-1))
# print(r1.scale(2))
'''
Задача 6: Класс для телефона
Напиши класс Phone, который хранит список вызовов (_calls).
Добавь методы add_call(call) и last_call(), которые работают с вызовами.

Алгоритм:

Создай класс Phone.
В методе __init__ создай пустой список _calls как защищенный атрибут .
Определи метод add_call(call), который добавляет вызов в список.
Определи метод last_call(), который возвращает последний вызов.
Убедись, что доступ к списку вызовов возможен только через методы.
'''
# class Phone:
#     def __init__(self, items):
#         self._calls = list(items)
#     def add_call(self, call):
#         self._calls.append(call)
#         return self._calls
#     def last_call(self):
#         return self._calls[-1]
#
#
# p1 = Phone([11, 22, 33, 44])
# print(p1.add_call(55))
# print(p1.last_call())
'''
Задача 7: Класс для студента
Напиши класс Student, который хранит список оценок (_grades).
Добавь методы add_grade(grade) и average_grade(), которые работают с оценками.

Алгоритм:

Создай класс Student.
В методе __init__ создай пустой список _grades как защищенный атрибут .
Определи метод add_grade(grade), который добавляет оценку.
Определи метод average_grade(), который вычисляет среднюю оценку.
Убедись, что доступ к списку оценок возможен только через методы.
'''
# class Student:
#     def __init__(self):
#         self._grades = []
#     def add_grade(self, grade):
#         self._grades.append(grade)
#         return self._grades
#     def average_grade(self):
#         gr = 0
#         for el in self._grades:
#             gr += el
#         return gr / len(self._grades)
#
#
# st1 = Student()
# print(st1.add_grade(5))
# print(st1.add_grade(5))
# print(st1.add_grade(4))
# print(st1.add_grade(3))
# print(st1.average_grade())
'''
Задача 8: Класс для города
Напиши класс City, который хранит население (_population).
Добавь метод update_population(change), который изменяет население.

Алгоритм:

Создай класс City.
В методе __init__ сохрани параметр _population как защищенный атрибут .
Определи метод update_population(change), который:
Проверяет, что изменение населения не приводит к отрицательному значению.
Изменяет _population.
Убедись, что доступ к населению возможен только через методы.
'''
# class City:
#     def __init__(self, population):
#         self._population = population
#     def update_population(self, change):
#         if change < 0:
#             return "Население в воставшие скелеты превращать нельзя"
#         else:
#             self._population = change
#             return self._population
#
#
# c1 = City(2000000)
# print(c1.update_population(1700000))
# print(c1.update_population(-2))
'''
Задача 9: Класс для времени
Напиши класс Time, который хранит часы (_hours) и минуты (_minutes).
Добавь метод add_time(other_time), который прибавляет другое время.

Алгоритм:

Создай класс Time.
В методе __init__ сохрани параметры _hours и _minutes как защищенные атрибуты .
Определи метод add_time(other_time), который:
Складывает часы и минуты.
Обрабатывает переход через 24 часа.
Убедись, что доступ к времени возможен только через методы.
'''
# class Time:
#     def __init__(self, hours, minutes):
#         self._hours = hours
#         self._minutes = minutes
#     def add_time(self, other_time):
#         total_minutes = self._minutes + other_time._minutes
#         total_hours = self._hours + other_time._hours + total_minutes // 60
#         self._hours = total_hours % 24
#         self._minutes = total_minutes % 60
#         return f"{self._hours}:{self._minutes:02}"
#
#
# t1 = Time(10, 25)
# t2 = Time(6, 22)
# print(t1.add_time(t2))
'''
Задача 10: Класс для кофемашины
Напиши класс CoffeeMachine, который хранит количество воды (_water), кофе (_coffee) и молока (_milk).
Добавь метод make_coffee(type), который делает чашку кофе определенного типа.

Алгоритм:

Создай класс CoffeeMachine.
В методе __init__ сохрани параметры _water, _coffee и _milk как защищенные атрибуты .
Определи метод make_coffee(type), который:
Для эспрессо: -10 воды и -5 кофе.
Для капучино: -10 воды, -5 кофе и -10 молока.
Проверяет наличие ресурсов перед изготовлением кофе.
Убедись, что доступ к ресурсам возможен только через методы.
'''
# class CoffeeMachine:
#     def __init__(self, water, coffee, milk):
#         self._water = water
#         self._coffee = coffee
#         self._milk = milk
#     def make_coffee(self, type):
#         if type.lower() == "эспрессо":
#             if self._water < 10 or self._coffee < 5:
#                 return "Недостаточно ресурсов"
#             else:
#                 self._water -= 10
#                 self._coffee -= 5
#                 return "Наслаждаемся эспрессо!"
#         elif type.lower() == "капучино":
#             if self._water < 10 or self._coffee < 5 or self._milk < 10:
#                 return "Недостаточно ресурсов"
#             else:
#                 self._water -= 10
#                 self._coffee -= 5
#                 self._milk -= 10
#                 return "Наслаждаемся капучино!"
#
#
# cm = CoffeeMachine(15, 10, 10)
# print(cm.make_coffee("эспрессо"))
# print(cm.make_coffee("капучино"))
# print(cm.make_coffee("капучино"))
'''
===========Задачи на использование приватных атрибутов===========
'''

'''
Задача 1: Класс для банковского счета
Напиши класс BankAccount, который хранит баланс (__balance).
Добавь методы deposit(amount) и withdraw(amount), которые изменяют баланс. 
Если сумма превышает баланс, добавь сообщение "Недостаточно средств!".

Алгоритм:

Создай класс BankAccount.
В методе __init__ сохрани параметр __balance как приватный атрибут .
Определи метод deposit(amount), который:
Проверяет, что amount > 0.
Прибавляет сумму к __balance.
Определи метод withdraw(amount), который:
Проверяет, что amount <= __balance.
Вычитает сумму из __balance.
Если средств недостаточно, возвращает "Недостаточно средств!".
Убедись, что доступ к __balance возможен только через методы.
'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount <= 0:
            return "Так нельзя"
        else:
            self.__balance += amount
            return self.__balance
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Недостаточно средств!"
        else:
            self.__balance -= amount
            return self.__balance


ba = BankAccount(10000)
print(ba.deposit(0))
print(ba.deposit(220))
print(ba.withdraw(11000))
print(ba.withdraw(4000))
'''
Задача 2: Класс для пользователя
Напиши класс User, который хранит имя (name) и пароль (__password).
Добавь метод check_password(password_attempt), который проверяет корректность пароля.

Алгоритм:

Создай класс User.
В методе __init__ сохрани параметры name и __password как приватный атрибут .
Определи метод check_password(password_attempt), который:
Проверяет, совпадает ли password_attempt с __password.
Возвращает True или False.
Убедись, что доступ к __password возможен только через метод check_password().
'''
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    def check_password(self, password_attempt):
        if self.__password == password_attempt:
            return True
        else:
            return False


u1 = User("Алексей", "qwerty")
print(u1.check_password("qwerty"))
'''
Задача 3: Класс для книги
Напиши класс Book, который хранит название (title) и год выпуска (__year).
Добавь метод update_year(new_year), который обновляет год выпуска.

Алгоритм:

Создай класс Book.
В методе __init__ сохрани параметры title и __year как приватный атрибут .
Определи метод update_year(new_year), который:
Проверяет, что new_year > __year.
Обновляет значение __year.
Убедись, что доступ к __year возможен только через метод update_year().
'''
class Book:
    def __init__(self, title, year):
        self.title = title
        self.__year = year
    def update_year(self, new_year):
        if new_year > self.__year:
            self.__year = new_year
            return self.__year
        else:
            return "Нельзя"


b1 = Book("Пикник на обочине", 1979)
print(b1.update_year(1960))
print(b1.update_year(1980))
'''
Задача 4: Класс для автомобиля
Напиши класс Car, который хранит пробег (__mileage) и марку (brand).
Добавь метод drive(distance), который увеличивает пробег.

Алгоритм:

Создай класс Car.
В методе __init__ сохрани параметры __mileage (приватный) и brand.
Определи метод drive(distance), который:
Проверяет, что distance > 0.
Увеличивает __mileage на указанное расстояние.
Убедись, что доступ к __mileage возможен только через метод drive().
'''
class Car:
    def __init__(self, mileage, brand):
        self.__mileage = mileage
        self.brand = brand
    def drive(self, distance):
        if distance > 0:
            self.__mileage += distance
            return self.__mileage
        else:
            "Пробег в минус невозможен"


c1 = Car(1000, "Daewoo Nexia")
print(c1.drive(0))
print(c1.drive(200))
'''
Задача 5: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width) и высоту (height).
Создай приватный атрибут __area для хранения площади.
Добавь метод set_dimensions(width, height), который устанавливает размеры и пересчитывает площадь.

Алгоритм:

Создай класс Rectangle.
В методе __init__ сохрани параметры width и height.
Создай приватный атрибут __area для хранения площади.
Определи метод set_dimensions(width, height), который:
Проверяет, что width > 0 и height > 0.
Обновляет размеры.
Пересчитывает __area как width * height.
Убедись, что доступ к __area возможен только через метод set_dimensions().
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__area = 0
    def set_dimensions(self, width, height):
        if self.width > 0 and self.height > 0:
            self.width = width
            self.height = height
            self.__area = self.width * self.height
            return f"Новые размеры: {self.width} - {self.height}, площадь = {self.__area}"
        else:
            return "Так нельзя"


rec = Rectangle(4, 3)
print(rec.set_dimensions(2,3))
'''
Задача 6: Класс для телефона
Напиши класс Phone, который хранит номер (number) и список вызовов (__calls).
Добавь метод add_call(call), который добавляет новый вызов.

Алгоритм:

Создай класс Phone.
В методе __init__ сохрани параметр number и создай пустой список __calls как приватный атрибут .
Определи метод add_call(call), который добавляет вызов в список __calls.
Убедись, что доступ к __calls возможен только через метод add_call().
'''
class Phone:
    def __init__(self, number):
        self.number = number
        self.__calls = []
    def add_call(self, call):
        self.__calls.append(call)
        return self.__calls


ph = Phone(89604914701)
print(ph.add_call(123))
print(ph.add_call(898))
'''
Задача 7: Класс для студента
Напиши класс Student, который хранит имя (name) и список оценок (__grades).
Добавь метод add_grade(grade), который добавляет новую оценку.

Алгоритм:

Создай класс Student.
В методе __init__ сохрани параметр name и создай пустой список __grades как приватный атрибут .
Определи метод add_grade(grade), который добавляет оценку в список __grades.
Убедись, что доступ к __grades возможен только через метод add_grade().
'''
class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []
    def add_grade(self, grade):
        self.__grades.append(grade)
        return self.__grades


st = Student("Алексей")
print(st.add_grade(5))
print(st.add_grade(4))
'''
Задача 8: Класс для города
Напиши класс City, который хранит название (name) и население (__population).
Добавь метод update_population(change), который изменяет население.

Алгоритм:

Создай класс City.
В методе __init__ сохрани параметры name и __population как приватный атрибут .
Определи метод update_population(change), который:
Проверяет, что изменение населения не приводит к отрицательному значению.
Изменяет __population.
Убедись, что доступ к __population возможен только через метод update_population().
'''
class City:
    def __init__(self, name, population):
        self.name = name
        self.__population = population
    def update_population(self, change):
        if change < 0:
            return "Мертвые души уже не в моде"
        else:
            self.__population += change
            return self.__population


ci = City("Краснодар", 1000000)
print(ci.update_population(-9))
print(ci.update_population(50000))
'''
Задача 9: Класс для времени
Напиши класс Time, который хранит часы (hours) и минуты (__minutes).
Добавь метод add_time(other_time), который прибавляет другое время.

Алгоритм:

Создай класс Time.
В методе __init__ сохрани параметры hours и __minutes как приватный атрибут .
Определи метод add_time(other_time), который:
Складывает часы и минуты.
Обрабатывает переход через 60 минут и 24 часа.
Убедись, что доступ к __minutes возможен только через метод add_time().
'''
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.__minutes = minutes
    def add_time(self, other_time):
        total_minutes = self.__minutes + other_time.__minutes
        total_hours = self.hours + other_time.hours + total_minutes // 60
        total_hours = total_hours % 24
        total_minutes = total_minutes % 60
        return f"{total_hours}:{total_minutes}"

t1 = Time(10, 15)
t2 = Time(6, 11)
print(t1.add_time(t2))
'''
Задача 10: Класс для кофемашины
Напиши класс CoffeeMachine, который хранит количество воды (water), кофе (__coffee) и молока (milk).
Добавь метод make_coffee(type), который делает чашку кофе определенного типа.

Алгоритм:

Создай класс CoffeeMachine.
В методе __init__ сохрани параметры water, __coffee (приватный) и milk.
Определи метод make_coffee(type), который:
Для эспрессо: -10 воды и -5 кофе.
Для капучино: -10 воды, -5 кофе и -10 молока.
Проверяет наличие ресурсов перед изготовлением.
Убедись, что доступ к __coffee возможен только через метод make_coffee().
'''
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.__coffee = coffee
        self.milk = milk
    def make_coffee(self, cof):
        if cof.lower() == "эспрессо":
            if self.__coffee < 5 or self.water < 10:
                return "Недостаточно ресурсов!"
            else:
                self.__coffee -= 5
                self.water -= 10
                return "Наслаждайтесь ароматным эспрессо"
        elif cof.lower() == "капучино":
            if self.__coffee < 5 or self.water < 10 or self.milk < 10:
                return "Недостаточно ресурсов!"
            else:
                self.__coffee -= 5
                self.water -= 10
                self.milk -= 10
                return "Наслаждайтесь ароматным капучино"


cm = CoffeeMachine(10, 10, 10)
print(cm.make_coffee("эспрессо"))
print(cm.make_coffee("капучино"))