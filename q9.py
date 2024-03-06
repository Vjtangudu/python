import random as r
n,m = [int(x) for x in input('Enter the range: ').split(',')]
lst = []
for i in range(5):
    a=r.randint(n,m)
    lst.append(a)
print(lst)
