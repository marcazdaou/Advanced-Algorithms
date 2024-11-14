def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratio for each item
    value_weight_ratio = [(value / weight, weight, value) for weight, value in items]
    # Sort items based on value-to-weight ratio in descending order
    value_weight_ratio.sort(reverse=True)

    # Initialize variables
    total_value = 0
    remaining_capacity = capacity

    # Iterate through sorted items
    for ratio, weight, value in value_weight_ratio:
        # Take the entire item if possible
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            # Otherwise, take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += fraction * value
            break  # Knapsack capacity exhausted

    return int(total_value)  # Convert total value to an integer before returning


# Sample Input
items = [(10, 60), (20, 100), (30, 120)]
knapsack_capacity = 50

# Sample Output
print("Maximum Value:", fractional_knapsack(items, knapsack_capacity))  # Output: Maximum Value: 240