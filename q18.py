tuple1 = tuple(int(x) for x in input('Enter the Elements: ').split(','))
n = int(input('Enter the number to find: '))
print(tuple1)
for x in tuple1:
    if x == n:
        print(f'{n} exists in the tuple')
