'''
Задача 1: Класс для книги
Алгоритм:
Напиши класс Book, который хранит название (title), автора (author) и год выпуска (year). Добавь метод get_age(),
который возвращает возраст книги.
Создай класс Book.
В методе __init__ сохрани параметры title, author и year.
Определи метод get_age(), который вычислит разницу между текущим годом (например, 2023) и годом выпуска.
'''
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def get_age(self):
#         book_age = 2023 - self.year
#         return book_age
#
# book = Book("Град обреченный","Братья Стругацкие", 1987)
# print(f"Книге уже = {book.get_age()} лет")
'''
Задача 2: Класс для студента
Напиши класс Student, который хранит имя (name) и список оценок (grades). Добавь метод average_grade(),
который возвращает среднюю оценку.
Алгоритм:
Создай класс Student.
В методе __init__ сохрани параметры name и grades (список чисел).
Определи метод average_grade(), который вычислит среднее значение списка оценок.
'''
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average_grade(self):
#         summa = 0
#         count = len(self.grades)
#         for el in self.grades:
#             summa += el
#         average = summa / count
#         return average
#
#
# stud = Student("Алексей", [5, 5, 4, 3, 4])
# print(f"Среднее значение оценок = {stud.average_grade()}")
'''
Задача 3: Класс для автомобиля
Напиши класс Car, который хранит марку (brand), год выпуска (year) и пробег (mileage). 
Добавь метод drive(distance), который увеличивает пробег на указанное расстояние.
Алгоритм:
Создай класс Car.
В методе __init__ сохрани параметры brand, year и mileage.
Определи метод drive(distance), который добавляет distance к пробегу.
'''
# class Car:
#     def __init__(self, brand, year, mileage):
#         self.brand = brand
#         self.year = year
#         self.mileage = mileage
#     def distance(self, distance):
#         self.mileage += distance
#         return self.mileage
#
#
# car = Car("Deawoo Nexia", 2013, 33200)
# print(f"После пробега в 400км, текущей пробег стал равен: {car.distance(400)}")
'''
Задача 4: Класс для банковского счета
Напиши класс BankAccount, который хранит имя владельца (owner) и баланс (balance). 
Добавь метод withdraw(amount), который уменьшает баланс, если сумма не превышает его.
Алгоритм:
Создай класс BankAccount.
В методе __init__ сохрани параметры owner и balance.
Определи метод withdraw(amount), который проверяет, достаточно ли средств, и уменьшает баланс.
'''
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return f"Остаток на балансе = {self.balance}"
#
#         else:
#             return "Недостаточно средств"
#
#
# acc = BankAccount("Алексей", 7000)
# print(acc.withdraw(700))
# print(acc.withdraw(10000))
'''
Задача 5: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width) и высоту (height). 
Добавь метод is_square(), который возвращает True, если это квадрат, иначе False.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width и height.
Определи метод is_square(), который проверит равенство сторон.
'''
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def is_square(self):
#         if self.width == self.height:
#             return True
#         else:
#             return False
#
#
# rect = Rectangle(4,4)
# print(rect.is_square())
# rect2 = Rectangle(4, 5)
# print(rect2.is_square())
'''
Задача 6: Класс для точки
Напиши класс Point, который хранит координаты x и y. Добавь метод distance_to(other_point), который вычисляет расстояние до другой точки.
Алгоритм:
Создай класс Point.
В методе __init__ сохрани координаты x и y.
Определи метод distance_to(other_point), используя формулу расстояния между точками.
'''
# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance_to(self, other_point):
#         dx = other_point.x - self.x
#         dy = other_point.y - self.y
#         return math.sqrt(dx ** 2 + dy ** 2)
#
# p1 = Point(4, 7)
# p2 = Point(8, 9)
# distance = p1.distance_to(p2)
# print(distance)
'''
Задача 7: Класс для списка покупок
Напиши класс ShoppingList, который хранит список товаров (items). Добавь метод remove_item(item), который удаляет товар из списка.
Алгоритм:
Создай класс ShoppingList.
В методе __init__ создай пустой список items.
Определи метод remove_item(item), который удаляет товар из списка.
'''
# class ShoppingList:
#     def __init__(self, items):
#         self.list = list(items)
#     def remove_item(self, item):
#         if item in self.list:
#             self.list.remove(item)
#         return self.list
#
#
# sl = ShoppingList(["Помидор", "Чабрец", "Яблоки"])
# print(sl.remove_item("Чабрец"))
'''
Задача 8: Класс для человека
Напиши класс Person, который хранит имя (name) и возраст (age). Добавь метод celebrate_birthday(), который увеличивает возраст на 1.
Алгоритм:
Создай класс Person.
В методе __init__ сохрани параметры name и age.
Определи метод celebrate_birthday(), который увеличивает возраст.
'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def celebrate_birthday(self):
#         self.age += 1
#         return self.age
#
#
# h1 = Person("Алексей", 37)
# print(h1.celebrate_birthday())
'''
Задача 9: Класс для круга
Напиши класс Circle, который хранит радиус (radius). Добавь метод is_large(), 
который возвращает True, если площадь больше 100, иначе False.
Алгоритм:
Создай класс Circle.
В методе __init__ сохрани параметр radius.
Определи метод is_large(), который вычислит площадь и проверит условие.
'''
# from math import pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def is_large(self):
#         plo = pi * self.radius ** 2
#         if plo > 100:
#             return True
#         else:
#             return False
#
#
# c1 = Circle(4)
# print(c1.is_large())
# c2 = Circle(37)
# print(c2.is_large())
'''
Задача 10: Класс для треугольника
Напиши класс Triangle, который хранит стороны a, b, c. Добавь метод is_valid(), 
который проверяет, существует ли треугольник.
Алгоритм:
Создай класс Triangle.
В методе __init__ сохрани параметры a, b, c.
Определи метод is_valid(), который проверит сумму двух сторон с третьей.
'''

'''
Задача 11: Класс для магазина
Напиши класс Store, который хранит название (name) и список товаров (items). 
Добавь метод total_items(), который возвращает общее количество товаров.
Алгоритм:
Создай класс Store.
В методе __init__ сохрани параметр name и создай пустой список items.
Определи метод add_item(item) для добавления товара.
Определи метод total_items(), который подсчитывает длину списка.
'''

'''
Задача 12: Класс для фильма
Напиши класс Movie, который хранит название (title) и продолжительность (duration). 
Добавь метод is_long(), который возвращает True, если фильм длиннее 120 минут.
Алгоритм:
Создай класс Movie.
В методе __init__ сохрани параметры title и duration.
Определи метод is_long(), который проверит продолжительность.
'''

'''
Задача 13: Класс для животного
Напиши класс Animal, который хранит вид (species) и возраст (age). 
Добавь метод can_speak(), который возвращает True, если возраст больше 1.
Алгоритм:
Создай класс Animal.
В методе __init__ сохрани параметры species и age.
Определи метод can_speak(), который проверит возраст.
'''

'''
Задача 14: Класс для телефона
Напиши класс Phone, который хранит номер (number) и список вызовов (calls). 
Добавь метод add_call(call), который добавляет новый вызов.
Алгоритм:
Создай класс Phone.
В методе __init__ сохрани параметр number и создай пустой список calls.
Определи метод add_call(call), который добавляет вызов в список.
'''

'''
Задача 15: Класс для города
Напиши класс City, который хранит название (name) и население (population). 
Добавь метод is_megacity(), который возвращает True, если население больше 10 миллионов.
Алгоритм:
Создай класс City.
В методе __init__ сохрани параметры name и population.
Определи метод is_megacity(), который проверит население.
'''

'''
Задача 16: Класс для времени
Напиши класс Time, который хранит часы (hours) и минуты (minutes). 
Добавь метод add_time(other_time), который прибавляет другое время.
Алгоритм:
Создай класс Time.
В методе __init__ сохрани параметры hours и minutes.
Определи метод add_time(other_time), который складывает время.
'''

'''
Задача 17: Класс для кофемашины
Напиши класс CoffeeMachine, который хранит количество воды (water) и кофе (coffee). 
Добавь метод make_coffee(count), который делает несколько чашек кофе.
Алгоритм:
Создай класс CoffeeMachine.
В методе __init__ сохрани параметры water и coffee.
Определи метод make_coffee(count), который уменьшает ресурсы на count * 10.
'''

'''
Задача 18: Класс для пользователя
Напиши класс User, который хранит имя (name) и электронную почту (email). 
Добавь метод update_email(new_email), который обновляет email.
Алгоритм:
Создай класс User.
В методе __init__ сохрани параметры name и email.
Определи метод update_email(new_email), который меняет email.
'''

'''
Задача 19: Класс для прямоугольника
Напиши класс Rectangle, который хранит ширину (width) и высоту (height). 
Добавь метод scale(factor), который увеличивает размеры на указанный коэффициент.
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width и height.
Определи метод scale(factor), который умножает размеры на factor.
'''

'''
Задача 20: Класс для банковской карты
Описание:
Напиши класс CreditCard, который будет хранить номер карты (card_number) и баланс (balance). 
Добавь метод withdraw(amount), который уменьшает баланс на указанную сумму, если сумма не превышает текущий баланс.
Алгоритм:
Создай класс CreditCard.
В методе __init__ сохрани параметры card_number (число или строка) и balance (число).
Определи метод withdraw(amount), который:
Проверяет, достаточно ли средств на карте (amount <= self.balance).
Если средств достаточно, уменьшает баланс на amount.
Если средств недостаточно, выводит сообщение "Недостаточно средств!".
'''