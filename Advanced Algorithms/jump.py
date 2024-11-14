def can_jump(nums):
    # Initialize the farthest reachable index
    max_reachable = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current index is beyond the farthest reachable index, return False
        if i > max_reachable:
            return False

        # Update the farthest reachable index if the current index plus its jump length is greater
        max_reachable = max(max_reachable, i + nums[i])

        # If the farthest reachable index reaches or exceeds the end of the array, return True
        if max_reachable >= len(nums) - 1:
            return True

    return False


# Sample Input
nums = [2, 3, 1, 1, 4]

# Sample Output
print(can_jump(nums))  # Output: True