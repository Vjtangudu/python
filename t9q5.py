character = input("Enter a character: ")
def checkcharacter(character):
    if character.isalpha():
        print(f"{character} is a character")
    
def checkvowel(character):
    if character == 'a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U':
        print(f"{character} is a vowel also")
    else:
        print(f"{character} is a consonant")

checkcharacter(character)
checkvowel(character)