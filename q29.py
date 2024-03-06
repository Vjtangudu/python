sample_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_data = sorted(sample_data, key=lambda x: float(x[1]))
print("Sorted tuple:", sorted_data)
