
'''
3. 5 задач когда нужно использовать обязательные параметры
'''
'''
Задача 1: Сложение трех чисел
Напиши функцию, которая принимает три числа и возвращает их сумму.
Подсказка: Все три числа должны быть обязательными параметрами.
'''
def summa(a, b, c):
    d = a + b + c
    return d
print(summa(1, 1, 2))
'''
Задача 2: Вычитание двух чисел
Напиши функцию, которая принимает два числа и возвращает результат их вычитания.
Подсказка: Оба числа должны быть обязательными параметрами.
'''
def raznost(a, b):
    d = a - b
    return d
print(raznost(4, 1))
'''
Задача 3: Деление двух чисел
Напиши функцию, которая принимает два числа и возвращает результат их деления.
Подсказка: Оба числа должны быть обязательными параметрами. Не забудь обработать случай деления на ноль.
'''
def delenie(a, b):
    if b == 0:
        print("Нельзя делить на 0")
        return
    else:
        c = a / b
        return c
print(delenie(4, 2))
'''
Задача 4: Вычисление среднего арифметического
Напиши функцию, которая принимает список чисел и возвращает их среднее арифметическое.
Подсказка: Список чисел должен быть обязательным параметром. Используй функцию sum() и len().
'''
def average(nums):
    userList = nums.split()
    numbers = [int(num) for num in userList]
    summa = 0
    srednee = 0
    for el in numbers:
        summa = summa + el
    srednee = summa / len(numbers)
    return srednee
print(average("4 2 4"))
'''
Задача 5: Количество символов в строке
Напиши функцию, которая принимает строку и возвращает количество символов в этой строке.
Подсказка: Строка должна быть обязательным параметром. Используй функцию len().
'''
def strLen(text):
    stroka = len(text)
    return stroka
print(strLen("kvakvakva"))