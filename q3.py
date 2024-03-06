lst = [eval(x) for x in input('Enter the Elements: ').split(',')]
a=max(lst)
b=min(lst)
print(f'The position max of {a} is : ',lst.index(max(lst)))
print(f'The position min of {b} is : ',lst.index(min(lst)))
    
#print('The maximum and minimum of the list is : ',max(lst),min(lst))