def istriangle(a,b,c):
    if a+b>c and a+c>b and a+b>c:
        print("Is a Valid Triangle")
    else:
        print("Is not a vaild triangle")

a = int(input("Enter the side: "))
b = int(input("Enter the side: "))
c = int(input("Enter the side: "))
istriangle(a,b,c)