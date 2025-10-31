def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example
arr = [1, 2, 4, 5, 6]  
print("Missing number is:", find_missing_number(arr))
