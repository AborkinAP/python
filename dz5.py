# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = list(input('Введите текст  ').split())
f = 'абв'
for i in text:
    if f in i:
        text.remove(i)
print(" ".join(text))

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# программа для игры с конфетами человек против человека.
from random import randint
print('Условие задачи: На столе лежит S конфет.\n Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n За один ход можно забрать не более чем N конфет. Все конфеты оппонента достаются сделавшему последний ход.\n Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?')
s = int(input('Укажите общее число конфет S '))
n = int(input('Укажите максимальное число конфет, которых можно взять за раз N'))
print('Начинаем игру!\n')
while s > 1:
    print(f'Игрок 1, возьмите конфеты от 1 до {n} ')
    a = int(input())
    s-=a
    if s==1:
        print('Игрок 1 победил!')
    else:
        print(f'Осталось всего {s} конфет.\nИгрок 2, возьмите конфеты от 1 до {n}')
        b = int(input())
        s-=b
        if s==1:
             print('Игрок 2 победил!')

# a) Добавьте игру против бота
while s > 1:
    print(f'Игрок 1, возьмите конфеты от 1 до {n} ')
    a = int(input())
    s-=a
    if s==1:
        print('Игрок 1 победил!')
    else:
        print(f'Осталось всего {s} конфет.\n Бот, возьмите конфеты от 1 до {n}')
        b = randint(1, n+1)
        s-=b
        print(f'бот взял - {b} конфет.\nОсталось всего {s} конфет.')
        if s==1:
             print('Бот победил!')
# b) Подумайте как наделить бота ""интеллектом""
while s > 1:
    if s%(n+1) == 1:
        print(f'Игрок 1, возьмите конфеты от 1 до {n} ')
        a = int(input())
        s-=a
        if s==1:
            print('Игрок 1 победил!')
        else:
            print(f'Осталось всего {s} конфет.\n Бот, возьмите конфеты от 1 до {n}')
            b = (n+1)-a
            s-=b
            print(f'бот взял - {b} конфет.\nОсталось всего {s} конфет.')
            if s==1:
             print('Бот победил!')
    else:
        print(f'Игрок 1, возьмите конфеты от 1 до {n} ')
        a = int(input())
        s-=a
        if s==1:
            print('Игрок 1 победил!')
        else:
            print(f'Осталось всего {s} конфет.\n Бот, возьмите конфеты от 1 до {n}')
            b = randint(1, n+1)
            s-=b
            print(f'бот взял - {b} конфет.\nОсталось всего {s} конфет.')
            if s==1:
                print('Бот победил!')
# Создайте программу для игры в ""Крестики-нолики"".
desk = ['1','2','3',
        '4','5','6',
        '7','8','9']
def print_desk(desk):
    print(desk[0], end = " ")
    print(desk[1], end = " ")
    print(desk[2])
 
    print(desk[3], end = " ")
    print(desk[4], end = " ")
    print(desk[5])
 
    print(desk[6], end = " ")
    print(desk[7], end = " ")
    print(desk[8]) 

print(print_desk(desk))
count = 0
while count < 4:
    print('Первый игрок, введите число куда Вы хотите поставить "Х"')
    a = int(input())
    desk[a-1] = 'Х'
    print(print_desk(desk))
    if (desk[0]=='Х' and desk[1]=='Х'  and desk[2]=='Х') or (desk[3]=='Х' and desk[4]=='Х'  and desk[5]=='Х') or  (desk[6]=='Х' and desk[7]=='Х'  and desk[8]=='Х') or (desk[0]=='Х' and desk[3]=='Х'  and desk[6]=='Х') or (desk[1]=='Х' and desk[4]=='Х'  and desk[7]=='Х') or (desk[2]=='Х' and desk[5]=='Х'  and desk[8]=='Х') or  (desk[0]=='Х' and desk[4]=='Х'  and desk[8]=='Х') or (desk[2]=='Х' and desk[4]=='Х'  and desk[6]=='Х'):
        print('Выйграл первый игрок')
        break
    else:
        print('Второй игрок, введите число куда Вы хотите поставить "О"')
        b = int(input())
        desk[b-1] = 'O'
        print(print_desk(desk))
        if (desk[0]=='O' and desk[1]=='O'  and desk[2]=='O') or (desk[3]=='O' and desk[4]=='O'  and desk[5]=='O') or  (desk[6]=='O' and desk[7]=='O'  and desk[8]=='O') or (desk[0]=='O' and desk[3]=='O'  and desk[6]=='O') or (desk[1]=='O' and desk[4]=='O'  and desk[7]=='O') or (desk[2]=='O' and desk[5]=='O'  and desk[8]=='O') or  (desk[0]=='O' and desk[4]=='O'  and desk[8]=='O') or (desk[2]=='O' and desk[4]=='O'  and desk[6]=='O'):
            print('Выйграл второй игрок')
            break
        else:
            print(print_desk(desk))
            count+=1
if count >= 4:
    print('Ничья')
            
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open("string.txt", "r") as data:
    text = data.read()
print(text)
count = 1
total = ''
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count+=1
    else:
        total = total + text[i] + str(count)
        count = 1
if count > 1 or text[len(text)-2] != text[-1]:
    total = total + text[-1] + str(count)
print(total)

# восстановления данных
with open("string1.txt", "r") as data:
    text = data.read()
print(text)
number = ''
res = ''
for i in range(len(text)):
    if text[i].isalpha():
        number += text[i+1]
    else:
        res = res + text[i-1] * int(number)
        number = ''
print(res)