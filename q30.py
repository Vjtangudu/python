my_list = [1, 2, 3, (4, 5), 6, 7, 8]
count_until_tuple = 0
for element in my_list:
    if isinstance(element, tuple):
        break
    count_until_tuple += 1

print("Number of elements until tuple:", count_until_tuple)
