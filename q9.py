def is_magic_word(word):
    n = len(word)
    
    if not all(char.islower() for char in word):
        return False
    
    for i in range(n // 2):
        if i % 2 == 0 and word[i] >= word[n - 1 - i]:
            return False
        elif i % 2 != 0 and word[i] <= word[n - 1 - i]:
            return False
    
    return True

user_input = input("Enter a word: ")
result = is_magic_word(user_input)

if result:
    print(f"The word '{user_input}' is a magic word.")
else:
    print(f"The word '{user_input}' is not a magic word.")
