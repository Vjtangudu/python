def fibonacci(number):
    n1 = 0
    n2 = 1
    n = 0
    while(n<=number):
        n = n1 + n2
        n1 = n2
        n2 = n
        if n<=number:
            print(n,"\t")
    
number = int(input("Enter a number: "))
print('0\n1')
fibonacci(number)