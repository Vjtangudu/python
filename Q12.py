Amount = int(input("Enter the amount: "))
Year = int(input("Enter the number of years: "))
Rate = float(input("Enter the rate of interest: "))

SimpleInterset = (Amount*Year*Rate)/100
A = Amount * ((1 + Rate / 100)**Year)
CI = A - Amount
   

print("The simple interset is:", SimpleInterset)
print("The compound interset is:", CI)
