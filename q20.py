tuple1 = tuple(int(x) for x in input('Enter the Elements: ').split(','))
n = int(input('Enter the number to find you want to find index: '))
print(f'Index of {n} is',tuple1.index(n))