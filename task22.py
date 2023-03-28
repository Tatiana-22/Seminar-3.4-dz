'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.'''


quantity_N = int(input('Введите n количество элементов: '))
print(quantity_N)
quantity_M = int(input('Введите m количество элементов: '))
print(quantity_M)
elements_N = set()
elements_M = set()
for i in range(quantity_N):
    elements_N.add(input())
for y in range(quantity_M):
    elements_M.add(input())
print('Множество N:', elements_N)
print('Множество M:', elements_M)
set_N_M = elements_N.intersection(elements_M)
print(set_N_M)



