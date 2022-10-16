# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число N: '))
# a = 1
# for i in range(1, n+1):
#     a*=i
#     print(a, end=", ")

# from random import randint
# n = int(input('Введите число N: '))
# res = 1
# res = lambda i: i*for i in range(1, n+1)
# # lst = list(map(lambda x: x*res res=x*res, lst))
# print(lst)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list = [2, 3, 4, 5, 6]
# list1 = []
# a = round(len(list)/2 + 0.1)
# for i in range(a):
#     list1.append(list[i]*list[len(list)-1-i])
# print(list1)

lst = [2, 3, 4, 5, 6]
lst = list(filter(lambda i: i*lst[-1], lst))
# a = round(len(list)/2 + 0.1)
# for i in range(a):
#     list1.append(list[i]*list[len(list)-1-i])
print(lst)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Было
# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(1, len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(f'{list} -> сумма элементов на нечетных позициях: {sum}')

# Стало
# lst = [2, 3, 5, 9, 3]
# lst = sum([lst[i] for i in range(len(lst)) if i % 2 != 0])
# print(lst)

