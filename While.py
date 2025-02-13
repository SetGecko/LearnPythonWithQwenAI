# ==========================================Задачи с циклом while=======================================================
'''
Задача 1: Счетчик от 1 до 10
Напиши программу, которая выводит числа от 1 до 10 с помощью цикла while.
'''
number = 1
while number <= 10:
    print(number)
    number+=1
'''
Задача 2: Факториал числа
Напиши программу, которая запрашивает у пользователя число n и вычисляет его факториал с помощью цикла while.
'''
n = int(input("Введите число n: "))
factorial = 1
current = n
while current > 0:
    factorial *= current
    current -= 1
print(f"Факториал числа {n}: {factorial}")
'''
Задача 3: Сумма чисел от 1 до n
Напиши программу, которая запрашивает у пользователя число n и выводит сумму всех чисел от 1 до n с помощью цикла while.
'''
n = int(input("Введите число n: "))
count = 1
summ = 0
while count <= n:
    summ += count
    count += 1
print(f"Сумма всех чисел от 1 до {n} = {summ}")
'''
Задача 4: Вывод четных чисел от 1 до n
Напиши программу, которая запрашивает у пользователя число n и выводит все четные числа от 1 до n с помощью цикла while.
'''
n = int(input("Введите число n: "))
num = 1
while num <= n:
    if num % 2 == 0:
        print(num)
    num += 1
'''
Задача 5: Угадай число
Напиши программу, которая загадывает случайное число от 1 до 100 и просит пользователя угадать это число.
Программа должна подсказывать, больше ли загаданное число или меньше, используя цикл while.
'''
print("Игра угадай число")
rrr = random.randint(0, 100)
choice = 0
while choice != rrr:
    choice = int(input("Введите ваше число: "))
    if choice < rrr:
        print("Неверно, число больше чем Вы указали")
    elif choice > rrr:
        print("Неверно, число меньше чем Вы указали")
print("Конец игры")
# ======================================================================================================================