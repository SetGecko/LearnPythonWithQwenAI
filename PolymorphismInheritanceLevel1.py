#================Задачи на полиморфизм через наследование===============
'''
Задача 11: Классы животных
Напиши базовый класс Animal с методом speak(). Создай дочерние классы Dog и Cat, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс Animal с методом speak(), который возвращает "Животное издает звук".

Создай дочерний класс Dog, унаследованный от Animal.
Переопредели метод speak(), чтобы он возвращал "Гав!".

Создай дочерний класс Cat, унаследованный от Animal.
Переопредели метод speak(), чтобы он возвращал "Мяу!".

Создай список объектов (dog, cat) и вызови метод speak() для каждого.
'''
class Animal:
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"


dog = Dog()
cat = Cat()
animals = [dog, cat]
for el in animals:
    print(el.speak())
'''
Задача 12: Классы книг
Напиши базовый класс Book с методом get_info(). Создай дочерние классы Ebook и PaperBook, 
которые переопределяют этот метод.

Алгоритм:

Создай базовый класс Book с параметрами title и author в методе __init__.
Определи метод get_info(), который возвращает строку "Книга: [название], Автор: [автор]".

Создай дочерний класс Ebook, унаследованный от Book.
В методе __init__ класса Ebook добавь параметр file_format.
Переопредели метод get_info(), чтобы он включал формат книги.

Создай дочерний класс PaperBook, унаследованный от Book.
В методе __init__ класса PaperBook добавь параметр pages.
Переопредели метод get_info(), чтобы он включал количество страниц.

Создай список объектов (ebook, paperbook) и вызови метод get_info() для каждого.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return "Здесь возвращается информация о книге"

class Ebook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format
    def get_info(self):
        return f"Электронная книга: {self.title}, Автор: {self.author}, Формат: {self.file_format}"

class PaperBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    def get_info(self):
        return f"Печатная книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

eb = Ebook("Пикник на обочине", "Братья Стругацкие", "PDF")
pb = PaperBook("Гиперион", "Дэн Симонс", 400)
books = [eb, pb]
for b in books:
    print(b.get_info())
'''
Задача 13: Классы машин
Напиши базовый класс Car с методом start_engine(). Создай дочерние классы Truck и Sedan, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс Car с параметрами brand и year в методе __init__.
Определи метод start_engine(), который возвращает строку "Автомобиль [марка] запускает двигатель".

Создай дочерний класс Truck, унаследованный от Car.
Переопредели метод start_engine(), чтобы он возвращал строку "Грузовик [марка] запускает двигатель".

Создай дочерний класс Sedan, унаследованный от Car.
Переопредели метод start_engine(), чтобы он возвращал строку "Легковой автомобиль [марка] запускает двигатель".

Создай список объектов (truck, sedan) и вызови метод start_engine() для каждого.
'''
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def start_engine(self):
        return f"Автомобиль {self.brand} запускает двигатель"

class Truck(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)
    def start_engine(self):
        return f"Грузовик {self.brand} запускает двигатель"

class Sedan(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)
    def start_engine(self):
        return f"Легковой автомобиль {self.brand} запускает двигатель"


tr = Truck("Камаз", 1900)
sd = Sedan("Daewoo Nexia", 2000)
cars = [tr, sd]
for car in cars:
    print(car.start_engine())
'''
Задача 14: Классы телефонов
Напиши базовый класс Phone с методом call(). Создай дочерние классы Smartphone и BasicPhone, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс Phone с параметром number в методе __init__.
Определи метод call(), который возвращает строку "Звоню на [номер]".

Создай дочерний класс Smartphone, унаследованный от Phone.
Переопредели метод call(), чтобы он поддерживал видеозвонки.

Создай дочерний класс BasicPhone, унаследованный от Phone.
Переопредели метод call(), чтобы он выполнял только обычные звонки.

Создай список объектов (smartphone, basic_phone) и вызови метод call() для каждого.
'''
class Phone:
    def __init__(self, number):
        self.number = number
    def call(self):
        return f"Звоню на {self.number}"

class Smartphone(Phone):
    def __init__(self, number):
        super().__init__(number)
    def call(self):
        return f"Видеозвонок на {self.number}"

class BasicPhone(Phone):
    def __init__(self, number):
        super().__init__(number)
    def call(self):
        return f"Просто звоню на {self.number}"

sm = Smartphone(8900)
bp = BasicPhone(3900)
ph = [sm, bp]
for p in ph:
    print(p.call())
'''
Задача 15: Классы геометрических фигур
Напиши базовый класс Shape с методом area(). Создай дочерние классы Rectangle и Circle, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс Shape с методом area(), который возвращает строку "Вычисляю площадь".

Создай дочерний класс Rectangle, унаследованный от Shape.
В методе __init__ класса Rectangle добавь параметры width и height.
Переопредели метод area(), чтобы он возвращал width * height.

Создай дочерний класс Circle, унаследованный от Shape.
В методе __init__ класса Circle добавь параметр radius.
Переопредели метод area(), чтобы он возвращал 3.14 * radius ** 2.

Создай список объектов (rectangle, circle) и вызови метод area() для каждого.
'''
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2


re = Rectangle(2, 4)
ci = Circle(10)
fig = [re, ci]
for el in fig:
    print(el.area())
'''
Задача 16: Классы пользователей
Напиши базовый класс User с методом can_drive(). Создай дочерние классы Admin и Child, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс User с параметрами name и age в методе __init__.
Определи метод can_drive(), который возвращает True, если age >= 16.

Создай дочерний класс Admin, унаследованный от User.
Переопредели метод can_drive(), чтобы админ мог водить всегда.

Создай дочерний класс Child, унаследованный от User.
Переопредели метод can_drive(), чтобы ребенок не мог водить никогда.

Создай список объектов (admin, child) и вызови метод can_drive() для каждого.
'''
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False

class Admin(User):
    def can_drive(self):
        return True

class Child(User):
    def can_drive(self):
        return False


ad = Admin("Admin", 200)
ch = Child("Child", 100)
p = [ad, ch]
for el in p:
    print(el.can_drive())
'''
Задача 17: Классы учебных заведений
Напиши базовый класс School с методом add_student(). Создай дочерние классы University и Kindergarten, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс School с параметром students (список учеников) в методе __init__.
Определи метод add_student(student), который добавляет ученика в список.

Создай дочерний класс University, унаследованный от School.
Переопредели метод add_student(student, faculty), чтобы можно было указать факультет.

Создай дочерний класс Kindergarten, унаследованный от School.
Переопредели метод add_student(child, age), чтобы добавлять детей только до 7 лет.

Создай список объектов (university, kindergarten) и вызови метод add_student() для каждого.
'''
class School:
    def add_student(self):
        return "Добавление студента"

class University(School):
    def __init__(self, name, students, faculty):
        self.name = name
        self.students = list(students)
        self.faculty = faculty
    def add_student(self, student, faculty):
        if faculty == self.faculty:
            self.students.append(student)
            return f"Студент {student} добавлен на факультет {self.faculty}."
        else:
            return "Факультет не соответствует университету!"

class Kindergarten(School):
    def __init__(self, name, children):
        self.name = name
        self.children = list(children)
    def add_student(self, child, age):
        if age <= 7:
            self.children.append(child)
            return f"Ребенок {child} добавлен в детский сад."
        else:
            return "Возраст превышает допустимый для детского сада."


university = University("КГУ", [], "Физический факультет")
kindergarten = Kindergarten("Солнышко", [])

schools = [university, kindergarten]

university = University("КГУ", [], "Физический факультет")
print(university.add_student("Алексей", "Физический факультет"))
print(university.add_student("Иван", "Химический факультет"))


kindergarten = Kindergarten("Солнышко", [])
print(kindergarten.add_student("Маша", 5))
print(kindergarten.add_student("Петя", 10))

schools = [university, kindergarten]
for school in schools:
    if isinstance(school, University):
        print(school.add_student("Анна", "Физический факультет"))
    elif isinstance(school, Kindergarten):
        print(school.add_student("Тимур", 3))
'''
Задача 18: Классы банковских карт
Напиши базовый класс BankAccount с методом withdraw(). Создай дочерние классы SavingsAccount и CreditCard, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс BankAccount с параметром balance в методе __init__.
Определи метод withdraw(amount), который уменьшает баланс.

Создай дочерний класс SavingsAccount, унаследованный от BankAccount.
Переопредели метод withdraw(amount), чтобы оставалось хотя бы 10% баланса.

Создай дочерний класс CreditCard, унаследованный от BankAccount.
Переопредели метод withdraw(amount), чтобы проверять лимит.
Создай список объектов (savings_account, credit_card) и вызови метод withdraw() для каждого.
'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if self.balance < amount:
            return "Операция невозможна"
        else:
            self.balance -= amount
            return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def withdraw(self, amount):
        lim = (self.balance / 100) * 90
        if amount < lim:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"
        else:
            return "Нельзя снять больше 90% баланса"

class CreditCard(BankAccount):
    def __init__(self, balance, limit):
        super().__init__(balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.limit or amount > self.balance:  # Добавил проверку баланса
            return "Операция невозможна"
        else:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"

savings_account = SavingsAccount(10000)
credit_card = CreditCard(10000, 9000)
cards = [savings_account, credit_card]
for el in cards:
    print(el.withdraw(2000))
'''
Задача 19: Классы кофемашин
Напиши базовый класс CoffeeMachine с методом make_coffee(). Создай дочерние классы EspressoMachine и LatteMachine, которые переопределяют этот метод.

Алгоритм:

Создай базовый класс CoffeeMachine с параметрами water, coffee, milk в методе __init__.
Определи метод make_coffee(type), который делает обычный кофе.

Создай дочерний класс EspressoMachine, унаследованный от CoffeeMachine.
Переопредели метод make_coffee(), чтобы делать эспрессо.

Создай дочерний класс LatteMachine, унаследованный от CoffeeMachine.
Переопредели метод make_coffee(), чтобы делать капучино.

Создай список объектов (espresso_machine, latte_machine) и вызови метод make_coffee() для каждого.
'''
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_coffee(self):
        if self.water < 10 or self.coffee < 5:
            return "Недостаточно ресурсов"
        else:
            self.water -= 10
            self.coffee -= 5
            return "Наслаждайтесь кофе!"

class EspressoMachine(CoffeeMachine):
    def __init__(self, water, coffee, milk):
        super().__init__(water, coffee, milk)
    def make_coffee(self):
        if self.water < 10 or self.coffee < 10:
            return "Недостаточно ресурсов"
        else:
            self.water -= 10
            self.coffee -= 10
            return "Наслаждайтесь эспрессо!"


class LatteMachine(CoffeeMachine):
    def __init__(self, water, coffee, milk):
        super().__init__(water, coffee, milk)
    def make_coffee(self):
        if self.water < 10 or self.coffee < 10 or self.milk < 5:
            return "Недостаточно ресурсов"
        else:
            self.water -= 10
            self.coffee -= 10
            self.milk -= 5
            return "Наслаждайтесь капучино!"

es = EspressoMachine(10, 10, 10)
la = LatteMachine(10, 5,20)
cof = [es, la]
for el in cof:
    print(el.make_coffee())