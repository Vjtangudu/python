temp = eval(input('Enter the temperature : '))
unit = input('Enter the units Celsius or Fahrenheit : ')
if(unit == 'Celsius'):
    print('Fahrenheit = ',((temp*(9/5))+32))
else:
    print('Celsius = ',(((temp-32)*(9/5))))
          