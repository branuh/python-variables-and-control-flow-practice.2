def sum_of_numbers(nums):
    ##Calculates the sum of all numbers in a given list.

    total = 0
    for num in nums:
        total += num
    return total
nums = [1, 2, 3, 4, 5]
result = sum_of_numbers(nums)
print(result)