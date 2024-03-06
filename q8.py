import random as r
you = Tie = sys = 0
for i in range(1,6):
    user = input('Enter rock papper or sissors: ')
    comp = r.choice(['rock','papper','sissors'])
    if(comp==user):
        print('Tie')
        Tie+=1
    elif((user=='rock' and comp=='sissors') or
         (user=='papper' and comp=='rock') or
         (user=='sissors' and comp=='papper')):
        you+=1
        print('You Won')
    else:
        print('System Won')
        sys+=1
print(f'user={you},system={sys},Tie={Tie}')
if(you>sys):
    print('You Won over System')
elif(you>sys):
    print('System Won over You')
else:
    print("It's a Tie")

