def istriangle(a,b,c):
    if a+b+c == 180:
        print("Is a Valid Triangle")
    else:
        print("Is not a vaild triangle")

a = int(input("Enter the angle: "))
b = int(input("Enter the angle: "))
c = int(input("Enter the angle: "))
istriangle(a,b,c)