def reverse_strings(strings):
  #Reverses each string in a given list.


  reversed_strings = []
  for string in strings:
    reversed_string = string[::-1]
    reversed_strings.append(reversed_string)
  return reversed_strings


input_list = ["mango", "banana", "avocado"]
output_list = reverse_strings(input_list)
print(output_list)  # Output: ['elppa', 'ananab', 'yrrehc']