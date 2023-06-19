def factorial(number):
    result = 0
    i = number-1
    while(i>0):
        number = number * i
        i = i-1
    print(number)

number = int(input("Enter the number: "))
factorial(number)       