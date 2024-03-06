def print_diamond(height):
    # Upper part of the diamond
    for i in range(1, height, 2):
        spaces = " " * ((height - i) // 2)
        stars = "*" * i
        print(spaces + stars + spaces)

    # Lower part of the diamond
    for i in range(height, 0, -2):
        spaces = " " * ((height - i) // 2)
        stars = "*" * i
        print(spaces + stars + spaces)

if __name__ == "__main__":
    height = int(input("Enter the height of the diamond: "))
    print_diamond(height)

