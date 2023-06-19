def istriangle(a,b,c):
    if a == b == c:
        print("Is a Equilateral Triangle")
    elif a+b>c or a+c>b or b+c>a:
        print("Is a Isosceles triangle")
    else:
        print("Is a scalen triangle")

a = int(input("Enter the angle: "))
b = int(input("Enter the angle: "))
c = int(input("Enter the angle: "))
istriangle(a,b,c)