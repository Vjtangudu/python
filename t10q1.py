
def checkpalindrome(number):
    temp = number
    reversenum = 0
    while(temp>0):
        lastdigit = temp%10
        reversenum = reversenum * 10 + lastdigit
        temp = temp/10
    
    if(number == reversenum):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")

number = int(input("Enter a number: "))
checkpalindrome(number)