def getgrade(percentage):
    if percentage >= 90:
        print("A GRADE")
    elif percentage >= 80:
        print("B GRADE")
    elif percentage >= 70:
        print("C GRADE")
    elif percentage >= 60:
        print("D GRADE")
    elif percentage >= 40:
        print("E GRADE")
    else:
        print("FAIL")
def getpercentage(total):
    percentage = (total/500)*100
    getgrade(percentage)

total=0 
subjects = []
for i in range(5):
    Sub = int(input("Enter the marks: "))
    subjects.append(Sub)
print(subjects)
for i in subjects:
    total = total + i
print(total)
getpercentage(total)




