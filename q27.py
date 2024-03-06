sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
modified_list = [tuple(t[:-1] + (new_value,)) for t in sample_list]
print("Modified list:", modified_list)
