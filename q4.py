num = int(input('Enter the number : '))
num1 = 0
num2 = 1
next_num = num1+num2
print(num1,',',num2,end='')
for i in range(3,num+1):
    print(',',next_num,end='')
    num1 = num2
    num2 = next_num
    next_num = num1 + num2