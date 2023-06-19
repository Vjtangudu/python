character = input("Enter a character: ")
def checkcharacter(character):
    if character.isalpha():
        print(f"{character} is a character")
    elif character.isdigit():
        print(f"{character} is a digit")
    else:
        print(f"{character} is a special character")

checkcharacter(character)