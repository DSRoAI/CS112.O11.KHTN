def max_non_decreasing_length(arr, n):
    # Calculate cumulative sum from arr[0] to arr[i-1]
    cumulative_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + arr[i - 1]

    # Initialize arrays to store the maximum length and previous indices
    max_length = [0] * (n + 1)  # max_length[i] stores the maximum length when considering up to index i
    previous_index = [0] * (n + 2)  # previous_index[i] stores the previous index for a non-decreasing subarray ending at index i

    # Dynamic Programming approach
    for i in range(1, n + 1):
        previous_index[i] = max(previous_index[i], previous_index[i - 1])
        max_length[i] = max_length[previous_index[i]] + 1
        target = cumulative_sum[i] * 2 - cumulative_sum[previous_index[i]]

        # Update previous_index array
        j = previous_index[i] + 1
        while j <= n and cumulative_sum[j] < target:
            j += 1
        previous_index[j] = i

    # Return the maximum length
    return max_length[n]

# Input
n = int(input())
arr = list(map(int, input().strip().split()))

# Calculate and print the maximum length of the non-decreasing array achievable through the magical operations
result = max_non_decreasing_length(arr, n)
print(result)