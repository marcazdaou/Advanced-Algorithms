def merge_sorted_lists(lists):
    if not lists:
        return []

    def merge_two_lists(lst1, lst2):
        merged = []
        i = j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                merged.append(lst1[i])
                i += 1
            else:
                merged.append(lst2[j])
                j += 1
        merged.extend(lst1[i:])
        merged.extend(lst2[j:])
        return merged

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i == len(lists) - 1:
                merged_lists.append(lists[i])
            else:
                merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
        lists = merged_lists

    return lists[0]

# Test the function
k = 3
lists = [[1, 4, 6], [2, 3, 5], [0, 7, 8]]
print(merge_sorted_lists(lists))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]