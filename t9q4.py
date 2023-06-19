character = input("Enter a character: ")
def checkcharacter(character):
    if character.isalpha():
        print(f"{character} is a character")
    else:
        print(f"{character} is not a character")

checkcharacter(character)