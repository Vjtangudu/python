a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
print('Before Swapping: ''a:',a,'b:',b,'c:',c)
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print('After Swapping: ''a:',a,'b:',b,'c:',c)
