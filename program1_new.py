import math

a= input('Введите катеты треугольников: ')
a=[int(i) for i in a.split()]

if (len(a) % 2) != 0:
    print('Введите четное кол-во катетов')
    exit() 

k1=a[0::2]
k2=a[1::2]

for i in range(len(k1)):
   print(f'Треугольник {i+1} с катетами {k1[i]} и {k2[i]} имеет площадь {(k1[i]*k2[i])/2} и гипотенузу {round(math.sqrt(k1[i]**2+k2[i]**2), 2)}')