def leap_year(year):
    if (year%4 and year%100 and year%400) == 0:
        print(year," is a leap year")
    else:
        print(year," is not a leap year")

year = int(input("Enter the year: "))
leap_year(year)