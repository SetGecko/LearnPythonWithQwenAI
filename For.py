# ==================Задачи с циклом for=================
# # 1. Сумма чисел от 1 до n: Напишите программу, которая запрашивает у пользователя число n и выводит сумму всех чисел от 1 до n.
userInput = int(input("Введите число: ")) #
summ = 0
for el in range(1, userInput+1):
    summ += el
print(summ)

# # 2. Факториал числа: Напишите программу, которая запрашивает у пользователя число n и вычисляет его факториал.
userInput2 = int(input("Введите число: "))
factorial = 1
for el in range(1, userInput2+1):
    factorial *= el
print(factorial)
#
# # 3. Таблица умножения: Напишите программу, которая выводит таблицу умножения на число n
userInput3 = int(input("Введите число: "))
for i in range(1, 11):
    multuple = i * userInput3
    print(f"{i} * {userInput3} = {multuple}")
#
# # 4. Обработка списка: Напишите программу, которая принимает список чисел и выводит их квадраты.
userInput4 = input("Введите числа через пробел: ")
userList = userInput4.split()
numbers = [int(num) for num in userList]
squares = []
for el in numbers:
    square = el ** 2
    squares.append(square)
for i in squares:
    print(i)
#
# # 5. Четные числа: Напишите программу, которая выводит все четные числа от 1 до n
userInput5 = int(input("Введите число: "))
for i in range(1, userInput5):
    if i % 2 == 0:
        print(i)
# ======================================================================================================================