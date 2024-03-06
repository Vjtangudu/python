def replace_last_value(list_of_tuples):
  new_list_of_tuples = []
  for tuple in list_of_tuples:
    if tuple:
      new_list_of_tuples.append(tuple[:-1])
    else:
      new_list_of_tuples.append(tuple)
  return new_list_of_tuples
list_of_tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list_of_tuples = replace_last_value(list_of_tuples)
print(new_list_of_tuples)