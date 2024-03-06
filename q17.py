tuple1 = tuple(x for x in input('Enter the Elements: ').split(','))
seen = set()
repeated_items = set()

for item in tuple1:
    if item in seen:
        repeated_items.add(item)
    else:
        seen.add(item)

print("Repeated Items:", repeated_items)
