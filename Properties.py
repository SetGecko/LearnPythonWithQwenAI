'''
Что это такое?
Геттеры, сеттеры и делитеры — это специальные методы, которые позволяют:

Геттер (@property): Управляет чтением атрибута.
Сеттер (@атрибут.setter): Управляет записью атрибута.
Делитер (@атрибут.deleter): Управляет удалением атрибута.
Эти методы используются для:

Проверки данных перед их записью.
Сокрытия внутренней реализации атрибута.
Добавления дополнительной логики при работе с атрибутом.

Пример: Класс для пользователя с возрастом
Задача:
Создать класс User, где возраст:

Не может быть отрицательным.
Не может превышать 120 лет.
При удалении устанавливается значение по умолчанию (0).
Решение:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # При инициализации автоматически вызывается сеттер

    # Геттер для age
    @property
    def age(self):
        return self._age  # Возвращает "скрытое" значение _age

    # Сеттер для age
    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError("Возраст должен быть между 0 и 120!")

    # Делитер для age
    @age.deleter
    def age(self):
        print("Возраст удален, устанавливаем значение по умолчанию.")
        self._age = 0  # При удалении возраста устанавливаем 0

# Создаем объект
user = User("Алексей", 37)

# Чтение (используется геттер)
print(user.age)  # Вывод: 37

# Запись (используется сеттер)
user.age = 40  # Проверка на корректность
print(user.age)  # Вывод: 40

# Удаление (используется делитер)
del user.age
print(user.age)  # Вывод: 0 (значение по умолчанию)

Как это работает?
Геттер (@property):
Метод age() без сеттера/делитера работает как геттер .

@property
def age(self):
    return self._age

Сеттер (@age.setter):
Метод с декоратором @age.setter управляет записью значения.

@age.setter
def age(self, value):
    if 0 <= value <= 120:
        self._age = value
    else:
        raise ValueError("Некорректный возраст!")

Делитер (@age.deleter):
Метод с декоратором @age.deleter управляет удалением атрибута.

@age.deleter
def age(self):
    self._age = 0  # Устанавливаем значение по умолчанию

Как использовать: del user.age → автоматически вызывается делитер.

Почему это нужно?
Проверка данных:
Сеттер позволяет проверять корректность данных перед записью.
Пример: user.age = -5 → вызовет ошибку.
Инкапсуляция:
Атрибут _age "скрыт" от прямого доступа. Внешний код работает с user.age, а не с _age.
Дополнительная логика:
Геттер/сеттер могут выполнять вычисления. Например, хранить возраст в днях, но возвращать в годах.
Как это связано со свойствами (@property)?
Свойство — это комбинация геттера, сеттера и делитера, которая позволяет:

Обращаться к атрибуту как к обычной переменной.
При этом скрыть его реализацию и добавить защиту.
Еще примеры
Пример 1: Класс для пароля
class Password:
    def __init__(self, password):
        self.password = password  # Автоматически вызывается сеттер

    @property
    def password(self):
        return self._password  # Возвращаем хэшированный пароль

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self._password = hash(value)  # Хэшируем пароль перед сохранением
        else:
            raise ValueError("Пароль слишком короткий!")

user = Password("secure123")
print(user.password)  # Вывод: хэш-значение
user.password = "weak"  # ValueError: Пароль слишком короткий!

Пример 2: Класс для координат
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return (self.x**2 + self.y**2)**0.5  # Вычисляем расстояние на лету

p = Point(3, 4)
print(p.distance)  # Вывод: 5.0 (без сеттера/делитера)

class Person:
    def __init__(self, name):
        self.name = name  # Приватный атрибут (например, _name)

    @property
    def name(self):  # Геттер
        return self._name

    @name.setter
    def name(self, value):  # Сеттер для свойства "name"
        self._name = value.capitalize()

    @name.deleter
    def name(self):  # Делитер для свойства "name"
        del self._name
        print("Имя удалено!")

Имя xxx должно совпадать с именем свойства (например, name).
Если сеттер/делитер объявлены без геттера, это вызовет ошибку.
xxx — это не просто метка, а именно имя, через которое внешний код работает с атрибутом.
'''


'''
Задача 1: Свойство для возраста
Описание: Создай класс Person, который будет хранить возраст (age). 
Сеттер должен запрещать отрицательные значения, делитер — устанавливать возраст в 0.
Алгоритм:

Создай приватный атрибут _age.
Определи геттер @property age для чтения _age.
В сеттере @age.setter проверь: если value < 0 → сохранить 0, иначе value.
В делитере @age.deleter установи _age = 0.
'''
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value,int) and value < 0:
            return "Ошибка"
        else:
            self._age = value

    @age.deleter
    def age(self):
        self._age = 0
'''
Задача 2: Свойство для пароля
Описание: Создай класс User, который будет хранить пароль (password). 
Сеттер должен требовать длину пароля ≥8 символов.
Алгоритм:

Создай приватный атрибут _password.
Определи геттер @property password для чтения _password.
В сеттере @password.setter проверь: если len(value) < 8 → вывести ошибку, иначе сохранить.
В делитере @password.deleter установи _password = None.
'''
class User:
    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Пароль слишком короткий!")
        else:
            self._password = value

    @password.deleter
    def password(self):
        self._password = None
'''
Задача 3: Свойство для email
Описание: Создай класс Contact, который будет хранить email. Сеттер должен проверять наличие @ и .com.
Алгоритм:

Создай приватный атрибут _email.
Определи геттер @property email для чтения _email.
В сеттере @email.setter проверь: если в value нет @ или .com → вывести ошибку, иначе сохранить.
В делитере @email.deleter установи _email = None.
'''
class Contact:
    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or ".com" not in value:
            raise ValueError("Email должен содержать @ и .com")
        else:
            self._email = value

    @email.deleter
    def email(self):
        self._email = None
'''
Задача 4: Свойство для координат
Описание: Создай класс GPS, который будет хранить широту (latitude) и долготу (longitude). 
Сеттеры должны ограничивать значения диапазоном -180..180.
Алгоритм:

Создай приватные атрибуты _latitude и _longitude.
Для каждого атрибута определи:
Геттер @property.
Сеттер с проверкой: если value вне диапазона → сохранить 0, иначе value.
Делитер, устанавливающий значение в 0.
'''
class GPS:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-180 <= value <= 180):
            self._latitude = 0
        else:
            self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            self._longitude = 0
        else:
            self._longitude = value
'''
Задача 5: Свойство для баланса счета
Описание: Создай класс BankAccount, который будет хранить баланс (balance). 
Сеттер должен предотвращать отрицательный баланс.
Алгоритм:

Создай приватный _balance.
Геттер @property balance возвращает _balance.
В сеттере @balance.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @balance.deleter устанавливает _balance = 0.
'''
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            self._balance = 0
        else:
            self._balance = value

    @balance.deleter
    def balance(self):
        self._balance = 0

'''
    def __init__(self, number):
        if not number.startswith("+7") and not number.startswith("+1"):
            raise ValueError("Некорректный код страны!")
        self.number = number
'''

'''
Задача 6: Свойство для курса студента
Описание: Создай класс Student, который будет хранить курс (course). 
Сеттер должен разрешать только значения от 1 до 6.
Алгоритм:

Создай приватный _course.
Геттер @property course возвращает _course.
В сеттере @course.setter проверь: если value не в диапазоне 1–6 → сохранить 1, иначе value.
Делитер @course.deleter устанавливает _course = 1.
'''
class Student:
    def __init__(self, course):
            self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if 1 <= value <= 6:
            self._course = value
        else:
            self._course = 1

    @course.deleter
    def course(self):
        self._course = 1
'''
Задача 7: Свойство для года выпуска книги
Описание: Создай класс Book, который будет хранить год выпуска (year). 
Сеттер должен запрещать года в будущем.
Алгоритм:

Создай приватный _year.
Геттер @property year возвращает _year.
В сеттере @year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @year.deleter устанавливает _year = 2023.
'''
class Book:
    def __init__(self, year):
            self.year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value > 2023:
            self._year = 2023
        else:
            self._year = value

    @year.deleter
    def year(self):
        self._year = 2023
'''
Задача 8: Свойство для температуры
Описание: Создай класс Thermometer, который будет хранить температуру в Цельсиях (celsius). 
Сеттер должен предотвращать значения ниже -273°C.
Алгоритм:

Создай приватный _celsius.
Геттер @property celsius возвращает _celsius.
В сеттере @celsius.setter проверь: если value < -273 → сохранить -273, иначе value.
Делитер @celsius.deleter устанавливает _celsius = -273.
'''
class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273:
            self._celsius = -273
        else:
            self._celsius = value

    @celsius.deleter
    def celsius(self):
        self._celsius = -273
'''
Задача 9: Свойство для номера телефона
Описание: Создай класс Phone, который будет хранить номер (number). Сеттер должен требовать 11 цифр.
Алгоритм:

Создай приватный _number.
Геттер @property number возвращает _number.
В сеттере @number.setter проверь: если длина value ≠ 11 → вывести ошибку, иначе сохранить.
Делитер @number.deleter устанавливает _number = None.
'''
class Phone:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if len(str(value)) != 11:
            raise ValueError("Некорректноре число символов")
        else:
            self._number = value

    @number.deleter
    def number(self):
        self._number = None
'''
Задача 10: Свойство для населения города
Описание: Создай класс City, который будет хранить население (population). Сеттер должен запрещать отрицательное население.
Алгоритм:

Создай приватный _population.
Геттер @property population возвращает _population.
В сеттере @population.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @population.deleter устанавливает _population = 0.
'''
class City:
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if value < 0:
            self._population = 0
        else:
            self._population = value

    @population.deleter
    def population(self):
        self._population = 0
'''
Задача 11: Свойство для регистрации пользователя
Описание: Создай класс Profile, который будет хранить год регистрации (registration_year). 
Сеттер должен разрешать только прошлые годы.
Алгоритм:

Создай приватный _registration_year.
Геттер @property registration_year возвращает _registration_year.
В сеттере @registration_year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @registration_year.deleter устанавливает _registration_year = 2023.
'''
class Profile:
    def __init__(self, registration_year):
        self.registration_year = registration_year

    @property
    def registration_year(self):
        return self._registration_year

    @registration_year.setter
    def registration_year(self, value):
        if value > 2023:
            self._registration_year = 2023
        else:
            self._registration_year = value

    @registration_year.deleter
    def registration_year(self):
        self._registration_year = 2023
'''
Задача 12: Свойство для цены товара
Описание: Создай класс Product, который будет хранить цену (price). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _price.
Геттер @property price возвращает _price.
В сеттере @price.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @price.deleter устанавливает _price = 0.
'''
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            self._price = 0
        else:
            self._price = value

    @price.deleter
    def price(self):
        self._price = 0
'''
Задача 13: Свойство для зарплаты сотрудника
Описание: Создай класс Employee, который будет хранить зарплату (salary). 
Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _salary.
Геттер @property salary возвращает _salary.
В сеттере @salary.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @salary.deleter устанавливает _salary = 0.
'''
class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            self._salary = 0
        else:
            self._salary = value

    @salary.deleter
    def salary(self):
        self._salary = 0
'''
Задача 14: Свойство для оценки студента
Описание: Создай класс StudentGrade, который будет хранить оценку (grade). Сеттер должен разрешать только значения от 2 до 5.
Алгоритм:

Создай приватный _grade.
Геттер @property grade возвращает _grade.
В сеттере @grade.setter проверь: если value не в диапазоне 2–5 → сохранить 3, иначе value.
Делитер @grade.deleter устанавливает _grade = 3.
'''
class StudentGrade:
    def __init__(self, grade):
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 2 <= value <= 5:
            self._grade = 3
        else:
            self._grade = value

    @grade.deleter
    def grade(self):
        self._grade = 3

'''
Задача 15: Свойство для модели автомобиля
Описание: Создай класс CarModel, который будет хранить год модели (model_year). Сеттер должен разрешать только прошлые годы.
Алгоритм:

Создай приватный _model_year.
Геттер @property model_year возвращает _model_year.
В сеттере @model_year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @model_year.deleter устанавливает _model_year = 2023.
'''
class CarModel:
    def __init__(self, model_year):
        self.model_year = model_year

    @property
    def model_year(self):
        return self._model_year

    @model_year.setter
    def model_year(self, value):
        if value > 2023:
            self._model_year = 2023
        else:
            self._model_year = value

    @model_year.deleter
    def model_year(self):
        self._model_year = 2023