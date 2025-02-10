'''
Что такое полиморфизм?
Полиморфизм (от греческого "много форм") — это способность объектов разных классов реагировать на вызов одного и того
 же метода по-разному. Это означает, что метод может иметь разное поведение в зависимости от типа объекта,
 который его вызывает.

Например:

У класса Dog метод speak() может возвращать "Гав!".
У класса Cat тот же метод speak() может возвращать "Мяу!".

Зачем нужен полиморфизм?
Универсальность:
Полиморфизм позволяет писать общий код, который работает с объектами разных классов без необходимости знать их
конкретный тип.
Расширяемость:
Если ты добавишь новый класс (например, Bird), он тоже сможет использовать метод speak(), но с другой реализацией.
Простота поддержки:
Ты можешь изменять реализацию методов в дочерних классах, не затрагивая основной код программы.

Как работает полиморфизм?
Пример 1: Базовый полиморфизм
class Dog:
    def speak(self):
        return "Гав!"

class Cat:
    def speak(self):
        return "Мяу!"

# Создаем объекты разных классов
dog = Dog()
cat = Cat()

# Вызываем одинаковый метод
print(dog.speak())  # Вывод: Гав!
print(cat.speak())  # Вывод: Мяу!

Пример 2: Полиморфизм через наследование
class Animal:
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    def speak(self):  # Переопределяем метод
        return "Гав!"

class Cat(Animal):
    def speak(self):  # Переопределяем метод
        return "Мяу!"

# Создаем объекты разных классов
dog = Dog()
cat = Cat()

# Вызываем метод через родительский класс
animals = [dog, cat]
for animal in animals:
    print(animal.speak())  # Вывод: Гав!, затем Мяу!

Когда используется полиморфизм?
В работе с коллекциями:
Когда у тебя есть список объектов разных классов, но ты хочешь вызывать у них одинаковые методы.
В интерфейсных классах:
Например, если есть класс Shape (геометрическая фигура) с методом area(), то дочерние классы Rectangle и Circle
могут иметь разные реализации этого метода.
В функциях высшего порядка:
Например, функция process_animals(animals) может принимать список животных и вызывать у каждого метод speak(),
даже если они принадлежат к разным классам.

Пример с наследованием

Базовый класс:
class Vehicle:
    def start_engine(self):
        return "Двигатель запущен"

Дочерние классы:
class Car(Vehicle):
    def start_engine(self):  # Переопределение метода
        return "Автомобильный двигатель запущен"

class Truck(Vehicle):
    def start_engine(self):  # Переопределение метода
        return "Грузовик запускает двигатель"

Использование:
car = Car()
truck = Truck()

vehicles = [car, truck]

for vehicle in vehicles:
    print(vehicle.start_engine())  # Вывод: Автомобильный двигатель запущен, затем Грузовик запускает двигатель

Преимущества полиморфизма
Общие интерфейсы:
Разные классы могут иметь общие методы, что упрощает работу с ними.
Удобство расширения:
Если ты добавишь новый класс (например, Bus), он также сможет использовать метод start_engine().
Читаемость кода:
Полиморфизм делает код более понятным и организованным.

Пример:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Общий метод
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Общий метод
        return 3.14 * self.radius ** 2

# Преимущество: можно работать с разными классами одинаково
shapes = [Rectangle(4, 2), Circle(3)]

for shape in shapes:
    print(shape.area())  # Вывод: 8, затем 28.26
'''

# ==============Задачи на базовый полиморфизм=================
'''
Задача 1: Классы животных
Напиши класс Animal, который будет иметь метод say_sound(). Для разных животных этот метод должен выводить разные звуки.

Алгоритм:

Создай класс Dog с методом say_sound(), который возвращает "Гав!".
Создай класс Cat с методом say_sound(), который возвращает "Мяу!".
Создай список объектов (dog, cat) и вызови метод say_sound() для каждого.
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
Задача 2: Классы чисел
Напиши класс Number, который будет хранить число. Метод get_number() должен возвращать это число.

Алгоритм:

Создай класс Number с параметром num в методе __init__.
Определи метод get_number(), который возвращает self.num.
'''
class Number:
    def __init__(self, num):
        self.num = num
    def get_number(self):
        return self.num

n1 = Number(4)
print(n1.get_number())
'''
Задача 3: Классы машин
Напиши класс Car, который будет иметь метод start_engine(). 
Для разных типов машин этот метод должен возвращать разные строки.

Алгоритм:

Создай класс Truck с методом start_engine(), который возвращает "Грузовик запускает двигатель".
Создай класс Sedan с методом start_engine(), который возвращает "Легковой автомобиль запускает двигатель".
Создай список объектов (truck, sedan) и вызови метод start_engine() для каждого.
'''
class Car:
    def start_engine(self):
        return "Машинка запускается"

class Truck(Car):
    def start_engine(self):
        return "Грузовик запускает двигатель"

class Sedan(Car):
    def start_engine(self):
        return "Легковой автомобиль запускает двигатель"


truck = Truck()
sedan = Sedan()
cars = [truck, sedan]
for car in cars:
    print(car.start_engine())
'''
Задача 4: Классы телефонов
Напиши класс Phone, который будет иметь метод call(). Для разных типов телефонов этот метод должен возвращать разные строки.

Алгоритм:

Создай класс Smartphone с методом call(), который возвращает "Выполняю видеозвонок".
Создай класс BasicPhone с методом call(), который возвращает "Выполняю обычный звонок".
Создай список объектов (smartphone, basic_phone) и вызови метод call() для каждого.
'''
class Phone:
    def call(self):
        return "Телефон звонит"

class Smartphone(Phone):
    def call(self):
        return "Выполняю видеозвонок"

class BasicPhone(Phone):
    def call(self):
        return "Выполняю обычный звонок"


smartphone = Smartphone()
basicPhone = BasicPhone()
phones = [smartphone, basicPhone]
for phone in phones:
    print(phone.call())
'''
Задача 5: Классы геометрических фигур
Напиши класс Shape, который будет иметь метод area(). Для разных фигур этот метод должен возвращать разные 
значения площади.

Алгоритм:

Создай класс Rectangle с параметрами width и height в методе __init__.
Определи метод area(), который возвращает self.width * self.height.
Создай класс Circle с параметром radius в методе __init__.
Определи метод area(), который возвращает 3.14 * self.radius ** 2.
Создай список объектов (rectangle, circle) и вызови метод area() для каждого.
'''
class Shape:
    def area(self):
        return "Здесь вычисляется площадь"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(4,2)
circ = Circle(4)
fig = [rect, circ]
for f in fig:
    print(f.area())
'''
Задача 6: Классы пользователей
Напиши класс User, который будет иметь метод can_drive(). 
Для разных типов пользователей этот метод должен возвращать разные значения.

Алгоритм:

Создай класс Admin с методом can_drive(), который всегда возвращает True.
Создай класс Child с параметром age в методе __init__.
Определи метод can_drive(), который возвращает False, если age < 16.
Создай список объектов (admin, child) и вызови метод can_drive() для каждого.
'''
class User:
    def can_drive(self):
        return "Здесь вернется инфо о возможности вождения"

class Admin(User):
    def can_drive(self):
        return True

class Child(User):
    def __init__(self, age):
        self.age = age
    def can_drive(self):
        if self.age >= 16:
            return True
        else:
            return False
ad = Admin()
ch = Child(13)
peo = [ad, ch]
for p in peo:
    print(p.can_drive())
'''
Задача 7: Классы книг
Напиши класс Book, который будет иметь метод get_info(). 
Для разных типов книг этот метод должен возвращать разные строки.

Алгоритм:

Создай класс Ebook с параметрами title, author и file_format в методе __init__.
Определи метод get_info(), который возвращает строку "Электронная книга: [название], Автор: [автор], Формат: [формат]".
Создай класс PaperBook с параметрами title, author и pages в методе __init__.
Определи метод get_info(), который возвращает строку "Печатная книга: [название], Автор: [автор], Страниц: [количество страниц]".
Создай список объектов (ebook, paperbook) и вызови метод get_info() для каждого.
'''
class Book:
    def get_info(self):
        return "Здесь возвращается информация о книге"
class Ebook(Book):
    def __init__(self, title, author, file_format):
        self.file_format = file_format
        self.title = title
        self.author = author
    def get_info(self):
        return f"Электронная книга: {self.title}, Автор: {self.author}, Формат: {self.file_format}"
class PaperBook(Book):
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_info(self):
        return f"Печатная книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


eb = Ebook("Пикник на обочине", "Братья Стругацкие", "PDF")
pb = PaperBook("Гиперион", "Дэн Симонс", 400)
books = [eb, pb]
for b in books:
    print(b.get_info())
'''
Задача 8: Классы городов
Напиши класс City, который будет иметь метод is_megacity(). Для разных типов городов этот метод должен возвращать разные значения.

Алгоритм:

Создай класс Capital с параметрами name и population в методе __init__.
Определи метод is_megacity(), который возвращает True, если population > 5_000_000.

Создай класс SmallCity с параметрами name и population в методе __init__.
Определи метод is_megacity(), который всегда возвращает False.

Создай список объектов (capital, small_city) и вызови метод is_megacity() для каждого.
'''
class City:
    def is_megacity(self):
        return "Информация о городе"

class Capital(City):
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def is_megacity(self):
        if self.population > 5000000:
            return True
        else:
            return False
class SmallCity(City):
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def is_megacity(self):
        return False


msk = Capital("Moscow",11000000)
tm = SmallCity("Timashevsk", 200000)
cit = [msk, tm]
for c in cit:
    print(c.is_megacity())
'''
Задача 9: Классы банковских счетов
Напиши класс BankAccount, который будет иметь метод withdraw(). 
Для разных типов счетов этот метод должен работать по-разному.

Алгоритм:

Создай класс SavingsAccount с параметром balance в методе __init__.
Определи метод withdraw(amount), который не позволяет снять больше 90% баланса.

Создай класс CreditCard с параметрами balance и limit в методе __init__.
Определи метод withdraw(amount), который проверяет лимит.

Создай список объектов (savings_account, credit_card) и вызови метод withdraw() для каждого.
'''
class BankAccount:
    def withdraw(self):
        return "Снятие средств"
class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        lim = (self.balance / 100) * 90
        if amount < lim:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"
        else:
            return "Нельзя снять больше 90% баланса"
class CreditCard(BankAccount):
    def __init__(self, balance, limit):
        self.limit = limit
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.limit and amount <= self.balance:
            self.balance -= amount
            return f"Снято {amount}. Новый баланс: {self.balance}"
        else:
            return "Операция невозможна!"

sa = SavingsAccount(15000)
cr = CreditCard(15000, 10000)
cards = [sa, cr]
for c in cards:
    print(c.withdraw(4000))
'''
Задача 10: Классы учебных заведений
Напиши класс School, который будет иметь метод add_student(). 
Для разных типов заведений этот метод должен работать по-разному.

Алгоритм:

Создай класс University с параметрами name и students в методе __init__.
Определи метод add_student(student, faculty), который добавляет студента только на указанный факультет.

Создай класс Kindergarten с параметрами name и children в методе __init__.
Определи метод add_student(child, age), который добавляет ребенка только если возраст <= 7.

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