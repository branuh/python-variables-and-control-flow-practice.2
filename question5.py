def print_even_value_keys(dictionary):
  ##Prints keys with even values from a dictionary.

  for key, value in dictionary.items():
    if value % 2 == 0:
      print(key)


my_dict = {'a': 5, 'b': 8, 'c': 10}
print_even_value_keys(my_dict)