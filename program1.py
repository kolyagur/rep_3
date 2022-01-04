import math

n=1

t_a = input('Введите катеты треугольников: ')
a = t_a.split()

if (len(a) % 2) != 0:
    print('Введите четное кол-во катетов')
    exit() 

kol=len(a)

while kol>0:
    print(f'Треугольник {n} с катетами {a[0]} и {a[1]} имеет площадь {(int(a[0])*int(a[1]))/2} и гипотенузу {math.sqrt(int(a[0])**2+int(a[1])**2)}')
    del a[:2]    
    n+=1
    kol=len(a)