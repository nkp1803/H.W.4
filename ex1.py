
'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются 
в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит 
сами элементы множеств.
'''

from random import randint
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
first_list = []
second_list = []
for i in range(n):
    number = randint(1,10)
    first_list.append(number)
print(first_list)
for i in range(m):
    number = randint(1,10)
    second_list.append(number)
print(second_list)

first_set = set(first_list)
print(first_set)
second_set = set(second_list)
print(second_set)
print()
result_set = first_set.intersection(second_set)
print(sorted(result_set))

