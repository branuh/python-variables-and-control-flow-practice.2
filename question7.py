def remove_duplicates(input_list):
  #Removes duplicates from a list.

  output_list = []
  for item in input_list:
    if item not in output_list:
      output_list.append(item)
  return output_list

my_list = [1, 2, 3, 2, 1, 4, 5, 4]
result = remove_duplicates(my_list)
print(result)