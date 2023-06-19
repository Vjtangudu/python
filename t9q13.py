basic_salary = int(input("Enter the basic salary: "))
def gross(basic_salary):
    if basic_salary <= 10000:
        HRA1 = basic_salary*(20/100)
        DA1 = basic_salary*(80/100)
        print("The Gross Salary is ",basic_salary+HRA1+DA1)
    elif basic_salary <= 20000:
        HRA1 = basic_salary*(25/100)
        DA1 = basic_salary*(90/100)
        print("The Gross Salary is ",basic_salary+HRA1+DA1)
    elif basic_salary > 20000:
        HRA1 = basic_salary*(30/100)
        DA1 = basic_salary*(95/100)
        print("The Gross Salary is ",basic_salary+HRA1+DA1)

gross(basic_salary)