lst = [eval(x) for x in input('Enter the Elements: ').split(',')]
lst.remove(max(lst))
lst.remove(min(lst))
print('The maximum and minimum of the list is : ',max(lst),min(lst))