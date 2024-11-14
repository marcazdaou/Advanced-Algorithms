def bubble_sort(activities):
    n = len(activities)
    for i in range(n):
        for j in range(0, n - i - 1):
            if activities[j][1] > activities[j + 1][1]:
                activities[j], activities[j + 1] = activities[j + 1], activities[j]

def max_activities_min_duration(activities):
    bubble_sort(activities)  # Sort activities by finish time
    selected_activities = []
    last_finish_time = float('-inf')
    total_duration = 0

    for activity in activities:
        start, finish = activity
        if start >= last_finish_time:  # If the activity doesn't overlap
            selected_activities.append(activity)
            last_finish_time = finish
            total_duration += finish - start

    return len(selected_activities)

# Sample Input
activities = [(1, 3), (2, 5), (4, 6), (7,9), (8, 10)]
# Output
print("Maximum Number of Activities:", max_activities_min_duration(activities))