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
Описание: Создай класс Person, который будет хранить возраст (age). Сеттер должен запрещать отрицательные значения, делитер — устанавливать возраст в 0.
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
Описание: Создай класс User, который будет хранить пароль (password). Сеттер должен требовать длину пароля ≥8 символов.
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
Описание: Создай класс GPS, который будет хранить широту (latitude) и долготу (longitude). Сеттеры должны ограничивать значения диапазоном -180..180.
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
    def gps(self):
        return f"latitude: {self._latitude}, longitude: {self._longitude}"

    @gps.setter
    def gps(self, value):
        if value > -180 and value < 180:
            self._latitude = value
            self._longitude = value
        else:
            self._latitude = 0
            self._longitude = 0

    @gps.deleter
    def gps(self):
        self._latitude = 0
        self._longitude = 0
'''
Задача 5: Свойство для баланса счета
Описание: Создай класс BankAccount, который будет хранить баланс (balance). Сеттер должен предотвращать отрицательный баланс.
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
Описание: Создай класс Student, который будет хранить курс (course). Сеттер должен разрешать только значения от 1 до 6.
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
Описание: Создай класс Book, который будет хранить год выпуска (year). Сеттер должен запрещать года в будущем.
Алгоритм:

Создай приватный _year.
Геттер @property year возвращает _year.
В сеттере @year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @year.deleter устанавливает _year = 2023.
'''

'''
Задача 8: Свойство для температуры
Описание: Создай класс Thermometer, который будет хранить температуру в Цельсиях (celsius). Сеттер должен предотвращать значения ниже -273°C.
Алгоритм:

Создай приватный _celsius.
Геттер @property celsius возвращает _celsius.
В сеттере @celsius.setter проверь: если value < -273 → сохранить -273, иначе value.
Делитер @celsius.deleter устанавливает _celsius = -273.
'''

'''
Задача 9: Свойство для номера телефона
Описание: Создай класс Phone, который будет хранить номер (number). Сеттер должен требовать 11 цифр.
Алгоритм:

Создай приватный _number.
Геттер @property number возвращает _number.
В сеттере @number.setter проверь: если длина value ≠ 11 → вывести ошибку, иначе сохранить.
Делитер @number.deleter устанавливает _number = None.
'''

'''
Задача 10: Свойство для населения города
Описание: Создай класс City, который будет хранить население (population). Сеттер должен запрещать отрицательное население.
Алгоритм:

Создай приватный _population.
Геттер @property population возвращает _population.
В сеттере @population.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @population.deleter устанавливает _population = 0.
'''

'''
Задача 11: Свойство для регистрации пользователя
Описание: Создай класс Profile, который будет хранить год регистрации (registration_year). Сеттер должен разрешать только прошлые годы.
Алгоритм:

Создай приватный _registration_year.
Геттер @property registration_year возвращает _registration_year.
В сеттере @registration_year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @registration_year.deleter устанавливает _registration_year = 2023.
'''

'''
Задача 12: Свойство для цены товара
Описание: Создай класс Product, который будет хранить цену (price). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _price.
Геттер @property price возвращает _price.
В сеттере @price.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @price.deleter устанавливает _price = 0.
'''

'''
Задача 13: Свойство для зарплаты сотрудника
Описание: Создай класс Employee, который будет хранить зарплату (salary). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _salary.
Геттер @property salary возвращает _salary.
В сеттере @salary.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @salary.deleter устанавливает _salary = 0.
'''

'''
Задача 14: Свойство для оценки студента
Описание: Создай класс StudentGrade, который будет хранить оценку (grade). Сеттер должен разрешать только значения от 2 до 5.
Алгоритм:

Создай приватный _grade.
Геттер @property grade возвращает _grade.
В сеттере @grade.setter проверь: если value не в диапазоне 2–5 → сохранить 3, иначе value.
Делитер @grade.deleter устанавливает _grade = 3.
'''

'''
Задача 15: Свойство для модели автомобиля
Описание: Создай класс CarModel, который будет хранить год модели (model_year). Сеттер должен разрешать только прошлые годы.
Алгоритм:

Создай приватный _model_year.
Геттер @property model_year возвращает _model_year.
В сеттере @model_year.setter проверь: если value > 2023 → сохранить 2023, иначе value.
Делитер @model_year.deleter устанавливает _model_year = 2023.
'''

'''
Задача 16: Свойство для веса
Описание: Создай класс Weight, который будет хранить вес (kg). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _kg.
Геттер @property kg возвращает _kg.
В сеттере @kg.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @kg.deleter устанавливает _kg = 0.
'''

'''
Задача 17: Свойство для высоты
Описание: Создай класс Height, который будет хранить рост (cm). Сеттер должен разрешать значения от 50 до 250 см.
Алгоритм:

Создай приватный _cm.
Геттер @property cm возвращает _cm.
В сеттере @cm.setter проверь: если value вне диапазона 50–250 → сохранить 170, иначе value.
Делитер @cm.deleter устанавливает _cm = 170.
'''

'''
Задача 18: Свойство для скорости
Описание: Создай класс Speed, который будет хранить скорость (km_h). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _km_h.
Геттер @property km_h возвращает _km_h.
В сеттере @km_h.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @km_h.deleter устанавливает _km_h = 0.
'''

'''
Задача 19: Свойство для процента
Описание: Создай класс Percentage, который будет хранить значение (value). Сеттер должен ограничивать диапазон 0–100.
Алгоритм:

Создай приватный _value.
Геттер @property value возвращает _value.
В сеттере @value.setter проверь: если value вне диапазона → сохранить 0, иначе value.
Делитер @value.deleter устанавливает _value = 0.
'''

'''
Задача 20: Свойство для процента заполнения бензобака
Описание: Создай класс FuelTank, который будет хранить процент заполнения (fill). Сеттер должен ограничивать диапазон 0–100.
Алгоритм:

Создай приватный _fill.
Геттер @property fill возвращает _fill.
В сеттере @fill.setter проверь: если value вне диапазона → сохранить 0, иначе value.
Делитер @fill.deleter устанавливает _fill = 0.
'''

'''
Задача 21: Свойство для количества страниц
Описание: Создай класс BookPages, который будет хранить количество страниц (pages). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _pages.
Геттер @property pages возвращает _pages.
В сеттере @pages.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @pages.deleter устанавливает _pages = 0.
'''

'''
Задача 22: Свойство для температуры
Описание: Создай класс Thermostat, который будет хранить температуру (temperature). Сеттер должен ограничивать диапазон 0–50°C.
Алгоритм:

Создай приватный _temperature.
Геттер @property temperature возвращает _temperature.
В сеттере @temperature.setter проверь: если value вне диапазона → сохранить 20, иначе value.
Делитер @temperature.deleter устанавливает _temperature = 20.
'''

'''
Задача 23: Свойство для количества товаров
Описание: Создай класс Inventory, который будет хранить количество товаров (count). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _count.
Геттер @property count возвращает _count.
В сеттере @count.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @count.deleter устанавливает _count = 0.
'''

'''
Задача 24: Свойство для уровня заряда
Описание: Создай класс Battery, который будет хранить уровень заряда (charge). Сеттер должен ограничивать диапазон 0–100%.
Алгоритм:

Создай приватный _charge.
Геттер @property charge возвращает _charge.
В сеттере @charge.setter проверь: если value вне диапазона → сохранить 100, иначе value.
Делитер @charge.deleter устанавливает _charge = 100.
'''

'''
Задача 25: Свойство для количества учеников
Описание: Создай класс Classroom, который будет хранить количество учеников (students). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _students.
Геттер @property students возвращает _students.
В сеттере @students.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @students.deleter устанавливает _students = 0.
'''

'''
Задача 26: Свойство для координат
Описание: Создай класс Coordinates, который будет хранить x и y. Сеттеры должны ограничивать значения диапазоном -1000..1000.
Алгоритм:

Создай приватные _x и _y.
Для каждого атрибута:
Геттер @property.
Сеттер с проверкой диапазона.
Делитер, устанавливающий значение в 0.
'''

'''
Задача 27: Свойство для процента湿度
Описание: Создай класс Humidity, который будет хранить влажность (percent). Сеттер должен ограничивать диапазон 0–100.
Алгоритм:

Создай приватный _percent.
Геттер @property percent возвращает _percent.
В сеттере @percent.setter проверь: если value вне диапазона → сохранить 50, иначе value.
Делитер @percent.deleter устанавливает _percent = 50.
'''

'''
Задача 28: Свойство для количества лайков
Описание: Создай класс Post, который будет хранить количество лайков (likes). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _likes.
Геттер @property likes возвращает _likes.
В сеттере @likes.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @likes.deleter устанавливает _likes = 0.
'''

'''
Задача 29: Свойство для количества страниц в журнале
Описание: Создай класс Magazine, который будет хранить количество страниц (pages). Сеттер должен предотвращать отрицательные значения.
Алгоритм:

Создай приватный _pages.
Геттер @property pages возвращает _pages.
В сеттере @pages.setter проверь: если value < 0 → сохранить 0, иначе value.
Делитер @pages.deleter устанавливает _pages = 0.
'''

'''
Задача 30: Свойство для уровня громкости
Описание: Создай класс Volume, который будет хранить уровень громкости (level). Сеттер должен ограничивать диапазон 0–100.
Алгоритм:

Создай приватный _level.
Геттер @property level возвращает _level.
В сеттере @level.setter проверь: если value вне диапазона → сохранить 50, иначе value.
Делитер @level.deleter устанавливает _level = 50.
'''