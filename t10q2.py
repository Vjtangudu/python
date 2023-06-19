
def interval(start,end):
    for number in range(start,end-1):
        if number%3 == 0 and number%5 == 0:
            print(number)

start = int(input("Enter the start Number: "))
end = int(input("Enter the end Number: "))

interval(start,end)