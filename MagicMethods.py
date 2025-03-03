'''
===================Магический метод __init__===================
Описание:
Конструктор класса. Вызывается при создании объекта для инициализации атрибутов.
Пример кода:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
Объяснение:
__init__ используется для подготовки объекта к работе, например, для установки начальных значений или
подключения внешних данных (файлы, БД).
'''

'''
Класс Book с инициализацией
Создай класс Book, который при инициализации сохраняет название, автора и год выпуска.
Алгоритм:
В __init__ добавь параметры title, author, year.
Сохрани их как атрибуты объекта.
'''
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
'''
Класс BankAccount с начальным балансом
Создай класс BankAccount, который при создании устанавливает начальный баланс и процентную ставку.
Алгоритм:
В __init__ добавь параметры balance и interest_rate.
Сохрани их как атрибуты.
'''
class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
'''
Класс Matrix с размерностью
Создай класс Matrix, который при инициализации принимает количество строк и столбцов и заполняет матрицу нулями.
Алгоритм:
В __init__ добавь параметры rows, cols.
Создай двумерный список размером rows x cols с нулями.
'''
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
'''
=================== Магический метод __str__ ===================
Описание:
Формирует строковое представление объекта для пользователя.

Пример кода:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Человек: {self.name}, {self.age} лет"

Объяснение:
__str__ полезен для понятного отображения объекта, например, при печати в логах или интерфейсе пользователя.
'''

'''
Класс Car для пользователей
Создай класс Car, который через __str__ выводит информацию в формате: "Марка: [brand], Год: [year]".
Алгоритм:
В __str__ верни строку с self.brand и self.year.
'''
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Марка: {self.brand}, Год: {self.year}"
'''
Класс Date для даты
Создай класс Date, который через __str__ формирует строку вида "DD-MM-YYYY".
Алгоритм:
В __str__ объедини self.day, self.month, self.year через дефис.
'''
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"
'''
Класс ShoppingList для списка товаров
Создай класс ShoppingList, который через __str__ выводит все товары через запятую.
Алгоритм:
В __str__ верни строку, объединяющую элементы списка self.items с разделителем ", ".
'''
class ShoppingList:
    def __init__(self, items):
        self.items = list(items)

    def __str__(self):
        return f"{self.items}"
'''
=================== Магический метод __repr__ ===================
Описание:
Формирует "официальное" строковое представление объекта для разработчиков.

Пример кода:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

Объяснение:
__repr__ помогает в отладке — например, при выводе объекта в списке или при работе в интерактивном режиме.
'''

'''
Класс Book для отладки
Создай класс Book, который через __repr__ возвращает строку: "Book(title='[title]', author='[author]')".
Алгоритм:
В __repr__ верни строку с self.title и self.author в формате для воссоздания объекта.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
'''
Класс Vector для отладки
Создай класс Vector, который через __repr__ показывает все координаты вектора.
Алгоритм:
В __repr__ верни строку вида "Vector(x=5, y=10)".
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
'''
Класс BankAccount для разработчика
Создай класс BankAccount, который через __repr__ выводит баланс и владельца.
Алгоритм:
В __repr__ верни строку: "BankAccount(owner='[owner]', balance=[balance])".
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"
'''
=================== Магический метод __add__ ===================
Описание:
Перегружает оператор + для сложения объектов.

Пример кода:
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)

Объяснение:
__add__ позволяет писать код естественно: вместо sum_resources(a, b) можно писать a + b.
'''

'''
Класс Time для сложения времени
Создай класс Time, который позволяет складывать объекты через + (например, 2 часа + 3 часа = 5 часов).
Алгоритм:
В __add__ верни новый объект Time с суммой self.hours + other.hours.
'''
class Time:
    def __init__(self, hours):
        self.hours = hours

    def __add__(self, other):
        if isinstance(other, Time):
            total_hours = self.hours + other.hours
            return Time(total_hours)  # Создаем новый объект Time
        else:
            raise ValueError("Складывать можно только объекты класса Time!")

    def __str__(self):
        return f"{self.hours} часов"
'''
Класс Inventory для объединения товаров
Создай класс Inventory, который через __add__ объединяет списки товаров из двух магазинов.
Алгоритм:
В __add__ верни новый список, объединяющий self.items и other.items.
'''
class Inventory:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        if isinstance(other, Inventory):
            total_items = self.items + other.items
            return Inventory(total_items)
        else:
            raise ValueError("Складывать можно только объекты класса Inventory!")

    def __str__(self):
        return f"Всего товаров: {', '.join(self.items)}"
'''
Класс Vector2D для сложения векторов
Создай класс Vector2D, который складывает векторы по координатам (x1 + x2, y1 + y2).
Алгоритм:
В __add__ верни новый вектор с суммой x и y.
'''
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector2D(new_x, new_y)
        else:
            raise ValueError("Можно складывать только векторы!")

    def __str__(self):
        return f"Вектор({self.x}, {self.y})"
'''
=================== Магический метод __eq__ ===================
Описание:
Перегружает оператор == для сравнения объектов.

Пример кода:
class Color:
    def __init__(self, code):
        self.code = code
    def __eq__(self, other):
        return self.code == other.code

Объяснение:
__eq__ нужен для работы с объектами в списках или словарях, например, для поиска дубликатов.
'''

'''
Сравнение книг по ISBN
Создай класс Book, который сравнивает книги по уникальному ISBN.
Алгоритм:
В __eq__ верни self.isbn == other.isbn.
Сравнение студентов по ID
'''
class Book:
    def __init__(self, isbn):
        self.isbn = isbn

    def __eq__(self, other):
        return self.isbn == other.isbn
'''
Создай класс Student, который считает студентов равными, если совпадает их ID.
Алгоритм:
В __eq__ верни self.id == other.id.
Сравнение точек на координатной плоскости
'''
class Student:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id
'''
Создай класс Point, который сравнивает точки по координатам x и y.
Алгоритм:
В __eq__ верни self.x == other.x and self.y == other.y.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
'''
=================== Магический метод __len__ ===================
Описание:
Возвращает длину объекта (например, количество элементов).

Пример кода:
class TaskList:
    def __init__(self):
        self.tasks = []
    def __len__(self):
        return len(self.tasks)

Объяснение:
__len__ позволяет использовать len() для объектов своих классов, как для списков или строк.
'''

'''
Длина списка задач
Создай класс TodoList, который через __len__ возвращает количество задач.
Алгоритм:
В __len__ верни len(self.tasks).
Длина списка товаров в магазине
'''
class TodoList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __len__(self):
        return len(self.tasks)
'''
Создай класс Store, который через __len__ возвращает количество товаров.
Алгоритм:
В __len__ верни len(self.items).
Длина строки в классе Text
'''
class Store:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
'''
Создай класс Text, который через __len__ возвращает длину сохранённой строки.
Алгоритм:
В __len__ верни len(self.content).
'''
class Text:
    def __init__(self, content):
        self.content = content

    def __len__(self):
        return len(self.content)
'''
=================== Магический метод __getitem__ ===================
Описание:
Делает объект индексируемым (например, object[0]).

Пример кода:
class Storage:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]

Объяснение:
__getitem__ полезен для работы с объектами как с коллекциями (например, cart[0] вернёт первый товар).
'''

'''
Доступ к элементам списка задач
Создай класс TaskList, который позволяет получать задачи по индексу.
Алгоритм:
В __getitem__ верни self.tasks[index].
Доступ к символам строки в классе Text
'''
class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __getitem__(self, item):
        return self.tasks[item]
'''
Создай класс Text, который позволяет получать символы строки по индексу.
Алгоритм:
В __getitem__ верни self.content[index].
Доступ к элементам списка товаров
'''
class Text:
    def __init__(self, content):
        self.content = content

    def __getitem__(self, item):
        return self.content[item]
'''
Создай класс ShoppingCart, который позволяет получать товары по индексу.
Алгоритм:
В __getitem__ верни self.items[index].
'''
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, item):
        return self.items[item]
'''
=================== Магический метод __setitem__ ===================
Описание:
Делает объект изменяемым через индекс (например, object[0] = value).

Пример кода:
class Storage:
    def __init__(self, data):
        self.data = data
    def __setitem__(self, index, value):
        self.data[index] = value

Объяснение:
__setitem__ нужен для имитации изменяемых структур (например, student.grades[0] = 5).
'''

'''
Изменение задачи в списке
Создай класс TaskList, который позволяет редактировать задачи по индексу.
Алгоритм:
В __setitem__ обнови self.tasks[index] = value.
'''
class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __setitem__(self, key, value):
        self.tasks[key] = value
'''
Изменение символов в строке класса Text
Создай класс Text, который позволяет менять символы строки по индексу.
Алгоритм:
В __setitem__ обнови self.content = self.content[:index] + value + self.content[index+1:].
'''
class Text:
    def __init__(self, content):
        self.content = content

    def __setitem__(self, key, value):
        self.content = self.content[:key] + value + self.content[key + 1:]
'''
Изменение товаров в корзине
Создай класс ShoppingCart, который позволяет заменять товары по индексу.
Алгоритм:
В __setitem__ обнови self.items[index] = value.
'''
class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, key, value):
        self.items[key] = value
'''
=================== Магический метод __call__ ===================
Описание:
Делает объект вызываемым как функция.

Пример кода:
class Counter:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        return self.count

Объяснение:
__call__ полезен для объектов-функций (например, кэширующие обёртки или декораторы).
'''

'''
Счётчик кликов
Создай класс ClickCounter, который увеличивает счётчик при каждом вызове.
Алгоритм:
В __call__ обнови self.count += 1.
'''
class ClickCounter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
'''
Калькулятор
Создай класс Calculator, который через __call__ выполняет сложение двух чисел.
Алгоритм:
В __call__(a, b) верни a + b.
'''
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, a, b):
        return self.a + self.b
'''
Таймер
Создай класс Timer, который через __call__ запускает таймер на указанное время.
Алгоритм:
В __call__(seconds) используй time.sleep(seconds).
'''
import time  # Импортируем модуль time для работы со временем


class Timer:
    def __call__(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise ValueError("Время должно быть числом!")

        if seconds < 0:
            raise ValueError("Время не может быть отрицательным!")

        print(f"Таймер запущен на {seconds} секунд.")
        time.sleep(seconds)
        print("Таймер завершился!")
'''
=================== Магический метод __del__ ===================
Описание:
Вызывается перед удалением объекта (срабатывает при del object).

Пример кода:
class Resource:
    def __del__(self):
        print("Ресурс уничтожен!")

Объяснение:
__del__ используется для очистки ресурсов (закрытие файлов, БД, сетевых соединений).
'''

'''
Уведомление о удалении файла
Создай класс File, который выводит сообщение при удалении объекта.
Алгоритм:
В __del__ напиши print(f"Файл {self.name} удалён").
'''
class File:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Файл {self.name} удалён")
'''
Освобождение памяти
Создай класс Memory, который при удалении объекта выводит информацию о высвобожденной памяти.
Алгоритм:
В __del__ напиши print(f"Освобождено {self.size} МБ").
'''
class Memory:
    def __init__(self, size):
        self.size = size

    def __del__(self):
        print(f"Освобождено {self.size} МБ")
'''
Закрытие соединения
Создай класс DatabaseConnection, который при удалении закрывает соединение с БД.
Алгоритм:
В __del__ вызови self.close_connection().
'''
class DatabaseConnection:
    def __init__(self, close_connection):
        self.close_connection = close_connection

    def __del__(self):
        print(f"Закрыто соединение с БД")
'''
=================== Магический метод __delitem__ ===================
Описание:
Удаляет элемент по индексу (срабатывает при del object[index]).

Пример кода:
class ListProxy:
    def __init__(self, data):
        self.data = data
    def __delitem__(self, index):
        del self.data[index]

Объяснение:
__delitem__ нужен для работы с объектами как с изменяемыми коллекциями (например, del cart[0]).
'''

'''
Удаление задачи из списка
Создай класс TaskList, который позволяет удалять задачи по индексу.
Алгоритм:
В __delitem__ удали self.tasks.pop(index).
'''
class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __delitem__(self, key):
        self.tasks.pop(key)
        return self.tasks
'''
Удаление товара из корзины
Создай класс ShoppingCart, который через __delitem__ удаляет товары.
Алгоритм:
В __delitem__ удали del self.items[index].
'''
class ShoppingCart2:
    def __init__(self, items):
        self.items = items

    def __delitem__(self, key):
        del self.items[key]
'''
Удаление символа из строки в классе Text
Создай класс Text, который позволяет удалять символы по индексу.
Алгоритм:
В __delitem__ обнови self.content = self.content[:index] + self.content[index+1:].
'''
class Text2:
    def __init__(self, content):
        self.content = content

    def __delitem__(self, key):
        self.content = self.content[:key] + self.content[key + 1:]
'''
=================== Магический метод __contains__ ===================
Описание:
Проверяет наличие элемента в объекте (срабатывает при element in object).

Пример кода:
class TaskList:
    def __init__(self):
        self.tasks = []
    def __contains__(self, task):
        return task in self.tasks

Объяснение:
__contains__ позволяет использовать in для проверки наличия элемента (например, if "яблоко" in store).
'''

'''
Поиск задачи в списке
Создай класс TaskList, который проверяет наличие задачи по её ID.
Алгоритм:
В __contains__(task_id) верни any(task.id == task_id for task in self.tasks).
'''
class TaskList2:
    def __init__(self, tasks):
        self.tasks = tasks  # Список задач

    def __contains__(self, task_id):
        return any(task.id == task_id for task in self.tasks)
'''
=================== Магический метод __iter__ ===================
Описание:
Делает объект итерируемым (срабатывает при for element in object).

Пример кода:
class TaskList:
    def __init__(self):
        self.tasks = []
    def __iter__(self):
        return iter(self.tasks)

Объяснение:
__iter__ нужен для работы с объектами как с коллекциями (например, for item in cart).
'''

'''
Итерация по задачам
Создай класс TaskList, который позволяет перебирать задачи через for.
Алгоритм:
В __iter__ верни итератор по self.tasks.
'''
class TaskList3:
    def __init__(self):
        self.tasks = []
    def __iter__(self):
        return iter(self.tasks)
'''
Итерация по товарам в магазине
Создай класс Store, который позволяет перебирать товары через for.
Алгоритм:
В __iter__ верни итератор по self.items.
'''
class Store2:
    def __init__(self):
        self.items = []
    def __iter__(self):
        return iter(self.items)
'''
Итерация по символам в тексте
Создай класс Text, который позволяет перебирать символы строки.
Алгоритм:
В __iter__ верни итератор по self.content.
'''
class Text3:
    def __init__(self):
        self.content = []
    def __iter__(self):
        return iter(self.content)
