lst = [eval(x) for x in input('Enter the Elements: ').split(',')]
n = int(input('Enter the number: '))
for x in lst:
    if x > n:
        print(x,end=' ')