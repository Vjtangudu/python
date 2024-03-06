lst = [eval(x) for x in input('Enter the Elements: ').split(',')]
even = []
odd = []
for x in lst:
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
print('Even List : ',even)
print('Odd List : ',odd)