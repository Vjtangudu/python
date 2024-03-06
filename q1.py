from random import randint

while True:
    num = eval(input('Enter a number between 1-5: '))
    num1 = randint(1,5)
    if(num == num1):
        print('Ya, you are right!!')
    else:
        print('No, the number is ',num1)
    
    go = input('If you want to continue Y/N: ')
    if(go == 'N' or go == 'n'):
        print('Thanks for playing')
        break