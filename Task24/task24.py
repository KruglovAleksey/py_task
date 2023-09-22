# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите количествово кустов: '))
gryadka = list(map(int, input(f'Введите количество ягона на каждом из {n} кустов через пробел: ').split()[:n]))
    
print(f'Количество ягот на кустах: {gryadka}')
a = int(input('Введите номер куста с которого собираются ягоды: '))
sum = 0
if a == len(gryadka):
    sum = gryadka[-2] + gryadka[-1] + gryadka[0]
elif a == 1:
    sum = gryadka[0] + gryadka[1] + gryadka[-1]
else:
    sum = gryadka[a-1] + gryadka[a-2] + gryadka[a]
print(f'{sum}, ягод собрано с кустов')