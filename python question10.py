def tuples_to_dict(tuple_list):
  #Converts a list of tuples to a dictionary.


  result_dict = {}
  for string, integer in tuple_list:
    result_dict[string] = integer
  return result_dict

my_tuples = [("apple", 5), ("banana", 3), ("cherry", 2)]
result_dict = tuples_to_dict(my_tuples)
print(result_dict)