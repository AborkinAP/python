# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
a = float(input('Введите вещественное число: '))
n = a
sum = 0
if n == 0:
    print(sum)
else:
    while n % 10 != 0:
        n *= 10
    n /= 10

while n != 0:
    sum += n % 10
    n = n//10
print(a, '->', round(sum))

# Пример:
# - 6782 -> 23
# - 0,56 -> 11


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число N: '))
a = 1
for i in range(1, n+1):
    a*=i
    print(a, end=", ")
  
# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Введите число N: '))
dic = {}
sum = 0
for i in range(1, n+1):
    dic[i] = round((1 + 1/n)**n)
    sum+=dic[i]
print(f'для n = {n}: {dic}, а сумма элементов = {sum}')
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

n = int(input('Введите количество элементов списка N: '))
a = int(input('Введите номер позиции списка : '))
b = int(input('Введите номер позиции списка : '))

list = []
for i in range(n):
    list.append(randint(-n, n))
print(list)

sum = 0
for i in range(1, n):
    if i == a or i == b:
        sum+=list[i-1]
for i in range(1, n):
    if i == b:
        sum+=list[i-1]
print(sum)


# Реализуйте алгоритм перемешивания списка.
from random import randint

n = int(input('Введите количество элементов списка N: '))
list = []
for i in range(n):
    list.append(randint(0, n))
print(list)

list1 = list
for i in range(len(list1)):
    rand_index = randint(0, len(list1)-1)
    temp = list1[i]
    list1[i] = list1[rand_index]
    list1[rand_index] = temp
print(list1)


