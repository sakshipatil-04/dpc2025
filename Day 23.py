from collections import deque

def sliding_window_maximum(arr, k):
    if not arr or k == 0:
        return []

    n = len(arr)
    result = []
    dq = deque()  

    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

test_cases = [
    {"arr": [1, 5, 3, 2, 4, 6], "k": 3},
    {"arr": [1, 2, 3, 4], "k": 2},
    {"arr": [7, 7, 7, 7], "k": 1}
]

for i, case in enumerate(test_cases, 1):
    arr, k = case["arr"], case["k"]
    output = sliding_window_maximum(arr, k)
    print(f"Test Case {i}: Input: arr = {arr}, k = {k} ➞ Output: {output}")
