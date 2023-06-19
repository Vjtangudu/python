character = input("Enter a character: ")
def checkcase(character):
    if character.isupper():
        print(f"{character} is in Upper case")
    else:
        print(f"{character} is not in lower case")

checkcase(character)