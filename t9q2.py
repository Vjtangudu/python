n = int(input("Enter Number: "))
if (n%5 and n%11) == 0:
    print(f"{n} is divisible by both 5 and 11")
else:
    print(f"{n} is not-divisible by both 5 and 11")