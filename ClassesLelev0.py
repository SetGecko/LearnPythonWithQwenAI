'''
Всегда ли должен быть метод __init__?
Нет, метод __init__ не всегда обязателен. Он используется для инициализации объекта при его создании.
Если тебе не нужно устанавливать начальные значения атрибутов, можно обойтись без него.

Всегда ли нужно указывать self?
Да, в методах класса параметр self всегда нужен (если только ты не используешь статические методы или методы класса, но это уже более сложная тема).
self позволяет методам работать с конкретным объектом класса.

class Person:
    def greet(self):
        return f"Привет, меня зовут {self.name}!"
'''

'''
Задача 1: Класс для приветствия
Напиши класс Greeter, который будет иметь метод say_hello(). Этот метод должен выводить строку "Привет!".
Алгоритм:
Создай класс Greeter.
Внутри класса определи метод say_hello().
В методе say_hello() используй print("Привет!").
Здесь нет необходимости в __init__, потому что мы не храним никаких данных
'''
class Greeter:
    def say_hello(self):
        print("Привет!")

test = Greeter()
print(test.say_hello())
'''
Задача 2: Класс для хранения имени
Напиши класс Person, который будет хранить имя человека. При создании объекта передавай имя через параметр name. Метод get_name() должен возвращать имя.
Алгоритм:
Создай класс Person.
В методе __init__ сохрани параметр name как атрибут объекта (self.name = name).
Определи метод get_name(), который будет возвращать значение self.name.
Используй __init__ для сохранения имени
self нужен для доступа к атрибутам объекта
'''
class Person:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

test = Person("Алексей")
print(test.get_name())

'''
Задача 3: Класс для счетчика
Напиши класс Counter, который будет иметь методы increment() (увеличивает счетчик на 1) и get_value() (возвращает текущее значение счетчика).
Алгоритм:
Создай класс Counter.
В методе __init__ установи начальное значение счетчика (self.value = 0).
Определи метод increment(), который увеличивает self.value на 1.
Определи метод get_value(), который возвращает значение self.value.
__init__ нужен для установки начального значения
self используется для работы с атрибутами объекта
'''
class Counter:
    def __init__(self, value):
        self.value = 0
    def increment(self):
        self.value += 1
    def get_value(self):
        return self.value
test = Counter(1)
print(test.get_value())
test2 = test.increment()
print(test.get_value())
'''
Задача 4: Класс для прямоугольника
Напиши класс Rectangle, который будет хранить ширину (width) и высоту (height). Метод get_area() должен возвращать площадь прямоугольника (width * height).
Алгоритм:
Создай класс Rectangle.
В методе __init__ сохрани параметры width и height как атрибуты объекта.
Определи метод get_area(), который вычисляет площадь (self.width * self.height).
__init__ нужен для сохранения width и height
self используется для доступа к атрибутам объекта
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
test = Rectangle(4, 2)
print(test.get_area())
'''
Задача 5: Класс для книги
Напиши класс Book, который будет хранить название (title) и автора (author). Метод get_info() должен возвращать строку формата "Книга: [название], Автор: [автор]".
Алгоритм:
Создай класс Book.
В методе __init__ сохрани параметры title и author как атрибуты объекта.
Определи метод get_info(), который формирует строку с информацией о книге.
__init__ нужен для сохранения title и author
self используется для доступа к атрибутам объекта
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Название книги: {self.title}.\nАвтор книги: {self.author}"
test = Book("Пикник на обочине","Братья Стругацкие")
print(test.get_info())

'''
Вопросы по задачам:
Задача №2
Ниже блок кода:
def __init__(self, name):
    self.name = name
 Я правильно понимаю следующую интерпретацию кода: обявляется метод который при запуске самого себя - то есть метода
 сохраняет в себе- self значение name? или как понять блок кода (self, name) ?

Ответы:
__init__:
Это специальный метод, который автоматически вызывается при создании нового объекта класса.
Он используется для инициализации (настройки) начальных значений атрибутов объекта.
(self, name):
self: Это ссылка на сам объект, который создается в данный момент. Через self ты можешь обращаться к атрибутам и методам этого объекта.
name: Это параметр, который передается при создании объекта. Например, когда ты пишешь Person("Алексей"), строка "Алексей" попадает в параметр name.
self.name = name:
Здесь ты сохраняешь значение параметра name как атрибут объекта (self.name).
После этого ты сможешь использовать self.name в других методах класса или получить доступ к нему через объект.


Задача №3
Я правильно понимаю, что пока я не использую test2 = test.increment() - то значение не изменится?

Задача 5 и остальные в методе init я пишу self.title = title - объясни пожалуйста зачем эта конструкция?

__init__ — это конструктор:
Он вызывается автоматически при создании объекта класса.
Используется для установки начальных значений атрибутов объекта.
self — это ссылка на объект:
Через self ты можешь сохранять параметры как атрибуты объекта.
Эти атрибуты можно использовать в других методах класса.


'''