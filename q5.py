lst = [eval(x) for x in input('Enter the Elements: ').split(',')]
lst1 = [eval(x) for x in input('Enter the Elements: ').split(',')]
if set(lst) & set(lst1):
    print(set(lst) & set(lst1))
