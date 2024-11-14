def max_activities(activities):
    # Sort activities based on finish times (using bubble sort)
    n = len(activities)
    for i in range(n):
        for j in range(0, n - i - 1):
            if activities[j][1] > activities[j + 1][1]:
                activities[j], activities[j + 1] = activities[j + 1], activities[j]

    # Initialize variables
    selected_activities = []
    previous_finish_time = float('-inf')

    # Iterate through sorted activities
    for activity in activities:
        start, finish = activity
        # Check if the current activity can be selected
        if start > previous_finish_time:
            selected_activities.append(activity)
            previous_finish_time = finish

    return len(selected_activities)


# Sample Input
activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5,9)]
# Sample Output
print(max_activities(activities))