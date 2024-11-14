def min_platforms(arrival, departure):
    # Manually sort arrival times
    for i in range(len(arrival)):
        for j in range(i + 1, len(arrival)):
            if arrival[i] > arrival[j]:
                arrival[i], arrival[j] = arrival[j], arrival[i]
                departure[i], departure[j] = departure[j], departure[i]

    # Initialize variables
    platforms_needed = 1
    max_platforms_needed = 1
    arrival_index = 1
    departure_index = 0

    # Iterate through arrival and departure times
    while arrival_index < len(arrival) and departure_index < len(departure):
        # If a train arrives before the departure of the current train
        if arrival[arrival_index] < departure[departure_index]:
            platforms_needed += 1
            arrival_index += 1
            # Update maximum platforms needed
            max_platforms_needed = max(max_platforms_needed, platforms_needed)
        else:  # If a train departs before the arrival of the next train
            platforms_needed -= 1
            departure_index += 1

    return max_platforms_needed


# Sample Input
arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]

# Sample Output
print("Minimum Platforms Required:",
      min_platforms(arrival_times, departure_times))  # Output: Minimum Platforms Required: 3