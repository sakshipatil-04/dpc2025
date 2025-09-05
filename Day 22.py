from collections import Counter

def first_element_to_repeat_k_times(arr, k):
 
    freq = Counter(arr)

    for num in arr:
        if freq[num] == k:
            return num
    return -1

test_cases = [
    {"arr": [2, 3, 4, 2, 2, 5, 5], "k": 2, "expected": 5},
    {"arr": [1, 1, 1, 1], "k": 1, "expected": -1},
    {"arr": [10], "k": 1, "expected": 10},
    {"arr": [6, 6, 6, 6, 7, 7, 8, 8, 8], "k": 3, "expected": 8},
]

for i, test in enumerate(test_cases, 1):
    result = first_element_to_repeat_k_times(test["arr"], test["k"])
    print(f"Test Case {i}: Expected = {test['expected']}, Got = {result}, {'✅' if result == test['expected'] else '❌'}")
