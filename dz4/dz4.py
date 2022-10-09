# Вычислить число c заданной точностью d
n = float(input('введите число '))
f = input('задайте точность d ')
m = 0
for i in f:
    if i != ".":
        m += 1
m -= 1
n = (int(n * (10**m))) / 10**m
print(f'{n}.')

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
lst = [7, 5, 3, 2]
n = int(input('введите число '))
a = n
lst1 = []
while n != 1:
    for i in lst:
        if n % i == 0:
            lst1.append(i)
            n /= i
print(lst1)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input('Задайте последовательность чисел ').split()))
lst1 = []
count = 0
for i in range(0, len(lst)):
    for j in range(0, len(lst)):
        if lst[i] == lst[j]:
            count += 1
    if count == 1:
        lst1.append(lst[i])
    count = 0
print(lst1)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
k = int(input("Введите натуральную степень k = "))
from random import randint
rand_lst = [randint(0, 101) for i in range(k+1)]


lst = rand_lst[::-1]
str_poly = ''
if len(lst) < 1:
        str_poly = 'x = 0'
else:
    for i in range(len(lst)):
        if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
            str_poly += f'{lst[i]}x^{len(lst)-i-1}'
            if lst[i+1] != 0:
                str_poly += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            str_poly += f'{lst[i]}x'
            if lst[i+1] != 0:
                str_poly += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            str_poly += f'{lst[i]} = 0'
        elif i == len(lst) - 1 and lst[i] == 0:
            str_poly += ' = 0'
print(str_poly)

with open('file.txt', 'w') as data:
    data.write(str_poly)


# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
