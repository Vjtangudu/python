from random import randint
while True:
    print('QUESTION')
    a = randint(1,10)
    b = randint(1,10)
    ans = eval(input(f'{a} x {b} = '))
    if((a*b) == ans):
        print('Ya, you are right!!')
    else:
        print('No, the answer is ',(a*b))
    go = input("Want to play again [y/n] : ")
    if go == "n" or go == "N":
        break
print('Thanks for playing')