from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # Step 1: Count the frequency of each element
    counter = Counter(nums)

    # Step 2: Create a list of buckets
    max_freq = max(counter.values())
    buckets = [[] for _ in range(max_freq + 1)]

    # Step 3: Distribute elements into buckets based on their frequency
    for num, freq in counter.items():
        buckets[freq].append(num)

    # Step 4: Collect elements from buckets starting from the highest frequency
    result = []
    for bucket in reversed(buckets):
        result.extend(bucket)
        if len(result) >= k:
            break

    # Step 5: Return the top k frequent elements
    return result[:k]
arr = [1, 1, 1, 1, 2, 2, 2, 3, 3]
k = 2
result = top_k_frequent(arr, k)
print("Top", k, "frequent elements:", result)  # Output: [1, 2]