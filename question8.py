def keys_with_values_greater_than_n(dictionary, n):
  #Returns keys with values greater than n.

  result = []
  for key, value in dictionary.items():
    if value > n:
      result.append(key)
  return result

my_dict = {'a': 8, 'b': 1, 'c': 13}
n = 5
keys_greater_than_n = keys_with_values_greater_than_n(my_dict, n)
print(keys_greater_than_n)