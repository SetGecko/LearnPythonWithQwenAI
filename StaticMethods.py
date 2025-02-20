'''
Что такое статический метод?
Статический метод — это метод класса, который не связан с конкретным экземпляром класса.
Он принадлежит самому классу и может вызываться без создания объекта этого класса.

Ключевые особенности:
Не использует self:
Статический метод не имеет доступа к атрибутам конкретного объекта (self), так как он работает на уровне самого класса.
Используется для общей логики:
Статические методы обычно используются для выполнения операций, которые не зависят от состояния объектов класса.
Обозначается декоратором @staticmethod:
Чтобы определить метод как статический, его нужно пометить декоратором @staticmethod.

Пример статического метода
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Вызываем статические методы без создания объекта
print(MathUtils.add(5, 3))  # Вывод: 8
print(MathUtils.multiply(4, 6))  # Вывод: 24

Что здесь происходит?
Класс MathUtils содержит два статических метода: add() и multiply().
Эти методы можно вызывать напрямую через имя класса (MathUtils.add()), не создавая объект класса.
Они выполняют общие математические операции, которые не зависят от состояния конкретного объекта.

Когда использовать статические методы?
Для общей функциональности:
Если метод не нуждается в доступе к атрибутам объекта, его можно сделать статическим. Например, проверка корректности данных:
class User:
    @staticmethod
    def is_valid_age(age):
        return age >= 0 and age <= 120

Для утилитарных функций:
Статические методы часто используются для реализации вспомогательных функций, связанных с классом:
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

Для группировки логики:
Статические методы позволяют объединять связанные функции внутри одного класса, даже если они не работают с объектами.
Доступ к `self`	Имеет доступ через self	Не имеет доступа к self
Создание объекта	Требует создания объекта класса	Можно вызывать без создания объекта
Использование	Работает с конкретным объектом	Выполняет общую задачу
Декоратор	Нет декоратора	Используется @staticmethod

Пример использования статического метода
Задача: Проверка возраста пользователя

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return age >= 0 and age <= 120

    def get_info(self):
        if self.is_valid_age(self.age):  # Можно вызвать статический метод через self
            return f"Имя: {self.name}, Возраст: {self.age}"
        else:
            return "Неверный возраст!"

print(User.is_valid_age(37))  # Вывод: True
user = User("Алексей", 37)
print(user.get_info())  # Вывод: Имя: Алексей, Возраст: 37

Преимущества статических методов
Экономия памяти:
Статический метод существует один на весь класс, независимо от количества объектов.
Ясность кода:
Если метод не работает с атрибутами объекта, использование @staticmethod делает намерение ясным.
Удобство использования:
Статические методы можно вызывать напрямую через имя класса, что иногда удобнее.
'''

'''
Задача 1: Проверка возраста
Описание: Напиши класс User, который имеет статический метод is_adult(age). 
Этот метод должен проверять, является ли человек совершеннолетним (возраст ≥18).

Алгоритм:

Создай класс User.
Определи статический метод is_adult(age) с помощью декоратора @staticmethod.
Если возраст больше или равен 18, верни True.
Иначе верни False.
'''
class User:
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False

print(User.is_adult(11))
print(User.is_adult(37))
'''
Задача 2: Проверка года выпуска автомобиля
Описание: Напиши класс Car, который имеет статический метод is_old(year). 
Этот метод должен проверять, является ли автомобиль старым (>10 лет от текущего года).

Алгоритм:

Создай класс Car.
Определи статический метод is_old(year) с помощью декоратора @staticmethod.
Вычисли возраст автомобиля как 2023 - year.
Если возраст больше 10, верни True.
Иначе верни False.
'''
class Car:
    @staticmethod
    def is_old(year):
        if (2023 - year) > 10:
            return True
        else:
            return False

print(Car.is_old(2013))
print(Car.is_old(2005))
'''
Задача 3: Проверка формата файла
Описание: Напиши класс File, который имеет статический метод is_valid_format(file_name). 
Этот метод должен проверять, допустим ли формат файла (pdf, docx, txt).

Алгоритм:

Создай класс File.
Определи статический метод is_valid_format(file_name) с помощью декоратора @staticmethod.
Извлеки расширение файла через file_name.split(".")[-1].
Если расширение входит в список допустимых (["pdf", "docx", "txt"]), верни True.
Иначе верни False.
'''
class File:
    @staticmethod
    def is_valid_format(file_name):
        if file_name.split(".")[-1] in (["pdf", "docx", "txt"]):
            return True
        else:
            return False

print(File.is_valid_format("zzz.txt"))
print(File.is_valid_format("222.jpg"))
'''
Задача 4: Проверка пароля
Описание: Напиши класс Password, который имеет статический метод is_strong(password). 
Этот метод должен проверять, достаточно ли надежный пароль (длина ≥8 символов).

Алгоритм:

Создай класс Password.
Определи статический метод is_strong(password) с помощью декоратора @staticmethod.
Если длина пароля больше или равна 8, верни True.
Иначе верни False.
'''
class Password:
    @staticmethod
    def is_strong(password):
        if len(password) >= 8:
            return True
        else:
            return False

print(Password.is_strong("asdasd"))
print(Password.is_strong("asdasdasdasd"))
'''
Задача 5: Конвертация температуры
Описание: Напиши класс Temperature, который имеет статический метод celsius_to_fahrenheit(celsius). 
Этот метод должен конвертировать градусы Цельсия в Фаренгейты.

Алгоритм:

Создай класс Temperature.
Определи статический метод celsius_to_fahrenheit(celsius) с помощью декоратора @staticmethod.
Вычисли температуру по формуле: (celsius * 9/5) + 32.
Верни результат.
'''
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(Temperature.celsius_to_fahrenheit(30))
'''
Задача 6: Проверка email
Описание: Напиши класс Email, который имеет статический метод is_valid(email). 
Этот метод должен проверять, содержит ли email символ @.

Алгоритм:

Создай класс Email.
Определи статический метод is_valid(email) с помощью декоратора @staticmethod.
Если в строке есть символ @, верни True.
Иначе верни False.
'''
class Email:
    @staticmethod
    def is_valid(email):
        return "@" in email

print(Email.is_valid("setgecko@gmail.com"))
print(Email.is_valid("setgeckogmail.com"))
'''
Задача 7: Вычисление площади прямоугольника
Описание: Напиши класс Rectangle, который имеет статический метод calculate_area(width, height). 
Этот метод должен вычислять площадь прямоугольника.

Алгоритм:

Создай класс Rectangle.
Определи статический метод calculate_area(width, height) с помощью декоратора @staticmethod.
Вычисли площадь как width * height.
Верни результат.
'''
class Rectangle:
    @staticmethod
    def calculate_area(width, height):
        if width != 0 and height !=0:
            return width * height
        else:
            return False

print(Rectangle.calculate_area(1, 0))
print(Rectangle.calculate_area(4, 2))
print(Rectangle.calculate_area(0, 0))
print(Rectangle.calculate_area(0, 2))
'''
Задача 8: Проверка дня недели
Описание: Напиши класс Weekday, который имеет статический метод is_weekend(day). 
Этот метод должен проверять, является ли день выходным (Saturday, Sunday).

Алгоритм:

Создай класс Weekday.
Определи статический метод is_weekend(day) с помощью декоратора @staticmethod.
Если день равен "Saturday" или "Sunday", верни True.
Иначе верни False.
'''
class Weekday:
    @staticmethod
    def is_weekend(day):
        if day == "Saturday" or day == "Sunday":
            return True
        else:
            return False

print(Weekday.is_weekend("Saturday"))
print(Weekday.is_weekend("Monday"))
'''
Задача 9: Конвертация валют
Описание: Напиши класс Currency, который имеет статический метод usd_to_rub(usd). 
Этот метод должен конвертировать доллары в рубли по курсу 80 рублей за доллар.

Алгоритм:

Создай класс Currency.
Определи статический метод usd_to_rub(usd) с помощью декоратора @staticmethod.
Вычисли сумму в рублях как usd * 80.
Верни результат.
'''
class Currency:
    @staticmethod
    def usd_to_rub(usd):
        if usd > 0:
            return usd * 80
        else:
            return False

print(Currency.usd_to_rub(10))
print(Currency.usd_to_rub(0))
'''
Задача 10: Проверка номера телефона
Описание: Напиши класс Phone, который имеет статический метод is_valid_number(number). 
Этот метод должен проверять, начинается ли номер с кода страны (+7 или +1).

Алгоритм:

Создай класс Phone.
Определи статический метод is_valid_number(number) с помощью декоратора @staticmethod.
Если номер начинается с "+7" или "+1", верни True.
Иначе верни False.
'''
class Phone:
    @staticmethod
    def is_valid_number(number):
        return number.startswith(("+7", "+1"))

print(Phone.is_valid_number("+411"))
print(Phone.is_valid_number("+79604914701"))