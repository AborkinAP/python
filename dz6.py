# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Было
# n = int(input('Введите число N: '))
# a = 1
# for i in range(1, n+1):
#     a*=i
#     print(a, end=", ")
# Стало
n = int(input('Введите число N: '))
fact = lambda x: 1 if x == 0 else x * fact(x - 1)
print(fact(n))

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Было
# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(1, len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(f'{list} -> сумма элементов на нечетных позициях: {sum}')

# Стало
lst = [2, 3, 5, 9, 3]
lst = sum([lst[i] for i in range(len(lst)) if i % 2 != 0])
print(lst)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Было
# lst = list(map(int, input('Задайте последовательность чисел ').split()))
# lst1 = []
# count = 0
# for i in range(0, len(lst)):
#     for j in range(0, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
#     if count == 1:
#         lst1.append(lst[i])
#     count = 0
# print(lst1)

# # Стало
lst = [int(i) for i in input().split()]
lst = list(filter(lambda i: lst.count(i) == 1, lst))
print(lst)

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Было
# text = list(input('Введите текст  ').split())
# f = 'абв'
# for i in text:
#     if f in i:
#         text.remove(i)
# print(" ".join(text))

# Стало
text = input('Введите текст  ').split()
f = 'абв'
lst = [i for i in text if f not in i]
print(" ".join(lst))