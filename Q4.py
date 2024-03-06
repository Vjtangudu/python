basic_sal = int(input('Enter the basic salary: '))
TA = (basic_sal*20)/100
print('TA = ',TA)
DA = (basic_sal*120)/100
print('DA = ',DA)
HRA = (basic_sal*30)/100
print('HRA = ',HRA)
print('Gross = ',(basic_sal+TA+DA+HRA))
