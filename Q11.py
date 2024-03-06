import math as m
a = int(input('Enter Side1: '))
b = int(input('Enter Side2: '))
c = int(input('Enter Side3: '))
S = (a+b+c)/2
print(S)
print(S*(S-a)*(S-b)*(S-c))
print('Area of triangle = ',m.sqrt(S*(S-a)*(S-b)*(S-c)))