leng = int(input('Enter the length : '))
high = int(input('Enter the height : '))
a=leng-2
for i in range(high):
    print('*'*leng)
    if(i==high-(high-1)):break
    for j in range(1,high-1):
        print('*'+' '*a+'*')
    
    
