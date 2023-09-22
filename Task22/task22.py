# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите колчиество элементов первого множества: '))
m = int(input('Введите колчиество элементов второго множества: '))

nset = list(map(int, input(f'Введите {n} целых чисел первого множества через пробел: ').split()[:n]))
mset = list(map(int, input(f'Введите {m} целых чисел второго множества через пробел: ').split()[:m]))
res = set.union(set(nset), set(mset))
print(f'Результат, элементы обеих множеств в порядне возрастания и без повторений: {sorted(res)}')
