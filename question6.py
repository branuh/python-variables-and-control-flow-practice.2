#Finds the largest number in a tuple.
def find_largest_number(numbers):

  # Initialize largest with the first number
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest


my_tuple = (10, 20, 30, 40, 50)
result = find_largest_number(my_tuple)
print(result)