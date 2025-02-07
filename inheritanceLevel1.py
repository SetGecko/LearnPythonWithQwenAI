'''
Что такое наследование?
Наследование — это механизм, при котором один класс (называемый дочерним или производным )
получает доступ ко всем атрибутам и методам другого класса (называемого родительским или базовым ).
При этом дочерний класс может:

Использовать все методы и атрибуты родительского класса.
Добавлять новые методы и атрибуты.
Переопределять (изменять) существующие методы родительского класса.

Зачем нужно наследование?
Реализация общей функциональности:
Если несколько классов имеют общие методы или атрибуты, можно вынести их в родительский класс,
чтобы не писать одинаковый код заново для каждого класса.
Создание специализированных классов:
Дочерние классы могут расширять или изменять поведение родительского класса, добавляя уникальные характеристики.
Улучшение читаемости и организации кода:
Наследование помогает сделать код более модульным и понятным, так как ты можешь группировать похожие классы вместе.
Повторное использование кода:
Вместо того чтобы писать одинаковые методы для разных классов, ты можешь просто унаследовать их от базового класса.

Когда обычно используется наследование?
При создании иерархий классов:
Например, если есть класс Animal (животное), то можно создать дочерние классы Dog (собака),
Cat (кошка) и Bird (птица), которые будут наследовать общие свойства (например, возраст, вид)
и методы (например, говорить).
При работе с разновидностями одного объекта:
Например, класс Car (машина) может быть базовым для классов Sedan, Truck и SUV,
которые будут иметь дополнительные характеристики.
При необходимости переопределения поведения:
Если базовый класс определяет общее поведение, а дочерние классы хотят его немного изменить, используй наследование.

Пример использования наследования
Базовый класс:
class Animal:
    def __init__(self, species, age):
        self.species = species  # Вид животного
        self.age = age          # Возраст

    def speak(self):
        return "Животное издает звук"

Дочерние классы:
class Dog(Animal):  # Класс Dog наследует от Animal
    def speak(self):  # Переопределяем метод speak()
        return "Гав!"

class Cat(Animal):  # Класс Cat наследует от Animal
    def speak(self):  # Переопределяем метод speak()
        return "Мяу!"

Использование классов:
dog = Dog("Собака", 5)
cat = Cat("Кошка", 3)

print(dog.speak())  # Вывод: Гав!
print(cat.speak())  # Вывод: Мяу!

print(dog.species)  # Вывод: Собака
print(cat.age)      # Вывод: 3

Важные моменты наследования
1. super():
Функция super() вызывает метод родительского класса.
Это полезно, когда ты хочешь использовать функциональность родительского класса, но также добавить что-то свое.
2. Переопределение методов:
Дочерний класс может переопределять методы родительского класса, чтобы изменить их поведение.
3. Множественное наследование:
Класс может наследоваться от нескольких классов одновременно.
Однако это может усложнить код, поэтому используй осторожно.
4. Уровни наследования:
Можно создавать цепочки наследования: класс A → класс B → класс C. Но слишком длинные цепочки могут привести к путанице.
'''

'''
Задача 1: Класс для животных
Напиши класс Animal, который имеет атрибут age (возраст) и метод speak(). Создай дочерний класс Dog, который:

Переопределяет метод speak() так, чтобы он возвращал строку "Гав!".
Добавляет метод is_puppy(), который проверяет, является ли собака щенком (возраст < 2).
Алгоритм:

Создай базовый класс Animal с методом speak(), который возвращает "Животное издает звук".
Создай дочерний класс Dog, унаследованный от Animal.
Переопредели метод speak() для вывода "Гав!".
Добавь метод is_puppy(), который проверяет возраст.
'''
class Animal:
    def __init__(self, age):
        self.age = age
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    def speak(self):
        return "Гав!"
    def is_puppy(self):
        if self.age < 2:
            return True
        else:
            return False


d1 = Dog(1)
print(d1.speak())
print(d1.is_puppy())
'''
Задача 2: Класс для книг
Напиши класс Book, который хранит название (title) и автора (author). Создай дочерний класс Ebook, который:

Добавляет атрибут file_format (например, "PDF").
Переопределяет метод get_info(), добавляя информацию о формате.
Алгоритм:

Создай базовый класс Book с методом get_info(), который возвращает строку "Книга: [название], Автор: [автор]".
Создай дочерний класс Ebook, унаследованный от Book.
Добавь атрибут file_format в метод __init__ класса Ebook.
Переопредели метод get_info(), чтобы он включал формат.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}"
class Ebook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format
    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Формат: {self.file_format}"


# eb1 = Book("Пикник на обочине", "Братья Стругацкие")
b1 = Ebook("Пикник на обочине", "Братья Стругацкие", "PDF")
print(b1.get_info())
'''
Задача 3: Класс для машин
Напиши класс Car, который хранит марку (brand) и год выпуска (year). Создай дочерний класс Truck, который:
Добавляет атрибут load_capacity (грузоподъемность).
Переопределяет метод start_engine(), добавляя сообщение "Грузовик запускает двигатель".
Алгоритм:

Создай базовый класс Car с методом start_engine(), который возвращает строку "Автомобиль запускает двигатель".
Создай дочерний класс Truck, унаследованный от Car.
Добавь атрибут load_capacity в метод __init__ класса Truck.
Переопредели метод start_engine() для грузовика.
'''
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def start_engine(self):
        return f"Автомобиль запускает двигатель"

class Truck(Car):
    def __init__(self, load_capacity):
        self.load_capacity = load_capacity
    def start_engine(self):
        return f"Грузовик запускает двигатель"


tr1 = Truck(200)
print(tr1.start_engine())
'''
Задача 4: Класс для пользователей
Напиши класс User, который хранит имя (name) и возраст (age). 
Создай дочерний класс Admin, который: Добавляет метод manage_system(), возвращающий строку "Управляю системой".
Переопределяет метод can_drive(), чтобы админ мог водить машину с любого возраста.
Алгоритм:

Создай базовый класс User с методами can_drive() (проверяет возраст >=16) и get_info().
Создай дочерний класс Admin, унаследованный от User.
Добавь метод manage_system().
Переопредели метод can_drive(), чтобы админ мог водить всегда.
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
    def __init__(self, age,name):
        super().__init__(age, name)
    def manage_system(self):
        return "Управляю системой"
    def can_drive(self):
        return True


ad1 = Admin("Ква",10)
print(ad1.manage_system())
print(ad1.can_drive())
'''
Задача 5: Класс для геометрических фигур
Напиши класс Shape, который имеет метод area(), возвращающий строку "Вычисляю площадь". 

Создай дочерний класс Rectangle, который:
Добавляет атрибуты width и height.
Переопределяет метод area(), чтобы он вычислял площадь прямоугольника.
Алгоритм:

Создай базовый класс Shape с методом area().
Создай дочерний класс Rectangle, унаследованный от Shape.
В методе __init__ класса Rectangle добавь параметры width и height.
Переопредели метод area(), чтобы он возвращал width * height.
'''
class Shape:
    def area(self):
        return "Вычисляю площадь"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


r1 = Rectangle(4, 2)
print(r1.area())
'''
Задача 6: Класс для телефонов
Напиши класс Phone, который хранит номер (number) и список вызовов (calls). 
Создай дочерний класс Smartphone, который:
Добавляет метод send_message(), возвращающий строку "Отправка сообщения".
Переопределяет метод call(), добавляя возможность видеозвонков.
Алгоритм:

Создай базовый класс Phone с методом call(), который возвращает строку "Звоню на [номер]".
Создай дочерний класс Smartphone, унаследованный от Phone.
Добавь метод send_message().
Переопредели метод call(), чтобы он поддерживал видеозвонки.
'''
class Phone:
    def call(self):
        return "Звоню на [номер]"

class Smartphone(Phone):
    def send_message(self):
        return True
    def call(self):
        return "Видеозвонок на [номер]"


sm1 = Smartphone()
print(sm1.call())
'''
Задача 7: Класс для городов
Напиши класс City, который хранит название (name) и население (population). Создай дочерний класс Capital, который:

Добавляет атрибут country (страна).
Переопределяет метод is_megacity(), чтобы столица считалась мегаполисом при населении >5 млн.
Алгоритм:

Создай базовый класс City с методом is_megacity(), проверяющим население >10 млн.
Создай дочерний класс Capital, унаследованный от City.
В методе __init__ класса Capital добавь параметр country.
Переопредели метод is_megacity() для столицы.
'''
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def is_megacity(self):
        if self.population > 10000000:
            return True
        else:
            return False

class Capital(City):
    def __init__(self, name, population, country):
        super().__init__(name, population)
        self.country = country
    def is_megacity(self):
        if self.population > 5000000:
            return True
        else:
            return False


cap = Capital("Москва", 7000000, "Россия")
print(cap.is_megacity())
'''
Задача 8: Класс для банковских счетов
Напиши класс BankAccount, который хранит баланс (balance). Создай дочерний класс SavingsAccount, который:

Добавляет метод add_interest(), начисляющий проценты на баланс.
Переопределяет метод withdraw(), чтобы нельзя было снять все средства.
Алгоритм:

Создай базовый класс BankAccount с методом withdraw().
Создай дочерний класс SavingsAccount, унаследованный от BankAccount.
Добавь метод add_interest().
Переопредели метод withdraw(), чтобы оставалось хотя бы 10% баланса.
'''
class BankAcccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if self.balance < amount:
            return "Недостаточно средств"
        else:
            self.balance -= amount
            return self.balance
class SavingsAccount(BankAcccount):
    def __init__(self, balance):
        super().__init__(balance)
    def add_interest(self):
        return True
    def withdraw(self, amount):
        if (self.balance/10) > (self.balance-amount):
            return "Недостаточно средств"
        else:
            self.balance -= amount
            return self.balance


ba = SavingsAccount(10000)
print(ba.withdraw(9500))
print(ba.withdraw(1000))
'''
Задача 9: Класс для кофемашин
Напиши класс CoffeeMachine, который хранит ресурсы (water, coffee, milk). 
Создай дочерний класс AdvancedCoffeeMachine, который:

Добавляет метод make_latte(), делающий латте.
Переопределяет метод refill(), чтобы можно было указать количество ресурсов для пополнения.
Алгоритм:

Создай базовый класс CoffeeMachine с методом make_coffee().
Создай дочерний класс AdvancedCoffeeMachine, унаследованный от CoffeeMachine.
Добавь метод make_latte().
Переопредели метод refill(), чтобы он принимал параметры для пополнения.
'''
class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_coffee(self):
        if self.water < 5 and self.coffee < 5 and self.milk < 5:
            return "Недостаточно ресурсов"
        else:
            self.water -= 5
            self.coffee -= 5
            self.milk -= 5
            return "Наслаждаемся кофе"


class AdvancedCoffeeMachine(CoffeeMachine):
    def __init__(self,water, coffee, milk):
        super().__init__(self, water, coffee, milk)
    def make_latte(self):
        if self.water < 10 and self.coffee < 5 and self.milk < 10:
            return "Недостаточно ресурсов"
        else:
            self.water -= 10
            self.coffee -= 5
            self.milk -= 10
            return "Наслаждаемся кофе"
    def refill(self, w, c, m):
        self.water += w
        self.coffee += c
        self.milk += m
        return "Ресурсы пополнены"
'''
Задача 10: Класс для учебных заведений
Напиши класс School, который хранит название (name) и список учеников (students).
 Создай дочерний класс University, который:

Добавляет атрибут faculty (факультет).
Переопределяет метод add_student(), чтобы можно было указать факультет студента.
Алгоритм:

Создай базовый класс School с методом add_student().
Создай дочерний класс University, унаследованный от School.
В методе __init__ класса University добавь параметр faculty.
Переопредели метод add_student(), чтобы он принимал факультет.
'''
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = list(students)
    def add_student(self, student):
        self.students.append(student)
        return self.students

class University(School):
    def __init__(self, name, students, faculty):
        super().__init__(name, students)
        self.faculty = faculty
    def add_student(self, student, faculty):
        if faculty == self.faculty:
            self.students.append(student)
            return f"Студент {student} добавлен на факультет {self.faculty}."
        else:
            return "Факультет не соответствует университету!"