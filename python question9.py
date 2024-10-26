def two_sum(nums, target):
  #Checks if two numbers in the list add up to the target.

  seen = set()
  for num in nums:
    complement = target - num
    if complement in seen:
      return True
    seen.add(num)
  return False

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))