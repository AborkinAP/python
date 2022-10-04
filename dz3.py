# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f'{list} -> сумма элементов на нечетных позициях: {sum}')

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2, 3, 4, 5, 6]
list1 = []
a = round(len(list)/2 + 0.1)
for i in range(a):
    list1.append(list[i]*list[len(list)-1-i])
print(list1)
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = [1.1, 1.2, 3.1, 5, 10.01]
list1 = []
for i in range(len(list)):
    a = round(list[i] % 1, 2)
    if a != 0:
        list1.append(a)
print(list1)

maxim = list1[0]
minim = list[0]
for i in range(1, len(list1)):
    if list1[i] > maxim:
        maxim = list1[i]
    else:
        if list1[i] < minim:
            minim = list1[i]

b = maxim - minim
print(f'{list} => {b}')

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input('введите число '))
list = []
while n > 0:
    if n % 2 > 0:
        list.append(1)
    else:
        list.append(0)
    n //= 2
print(list)

list.reverse()
print(list)
for i in list:
    print(i, end="")

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fib(n):
    if n < 0:
        return fib(n+2) - fib(n+1)
    elif n == 0:
        return 0
    elif n in [-1, 1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []
for e in range(-8, 8):
    list.append(fib(e))
print(list)
# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
