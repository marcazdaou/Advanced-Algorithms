def bucketSort(temperature_data):
    # Define the range of temperatures (-50 to 50 degrees Celsius)
    min_temp = -50
    max_temp = 50
    bucket_range = max_temp - min_temp + 1

    # Create empty buckets
    buckets = [[] for _ in range(bucket_range)]

    # Scatter elements into buckets
    for temp in temperature_data:
        index = temp - min_temp
        buckets[index].append(temp)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate buckets
    sorted_temperatures = [elem for bucket in buckets for elem in bucket]
    return sorted_temperatures

# Input temperature data
temperature_data = [10, 20, -5, 8, 12, 18, 5, -3, 0, 15]

# Perform bucket sort
sorted_temperatures = bucketSort(temperature_data)

# Output sorted temperatures
print("Sorted temperatures:", sorted_temperatures)