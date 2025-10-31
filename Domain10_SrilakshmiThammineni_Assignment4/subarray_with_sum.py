def subarray_with_sum(arr, S):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink window if sum exceeds S
        while current_sum > S and start < end:
            current_sum -= arr[start]
            start += 1

        # Check if sum equals S
        if current_sum == S:
            return [start, end]  # returning indices

    return -1


arr = [1, 2, 3, 7, 5]
S = 12
print(subarray_with_sum(arr, S))