from collections import deque, defaultdict

def shortest_path_length(V, edges, start, end):
    if start == end:
        return 0
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  

    visited = [False] * V
    queue = deque([(start, 0)])  

    while queue:
        current, dist = queue.popleft()
        if current == end:
            return dist
        if visited[current]:
            continue
        visited[current] = True
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append((neighbor, dist + 1))

    return -1

test_cases = [
    {
        "V": 5,
        "edges": [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]],
        "start": 0,
        "end": 4,
        "expected": 3
    },
    {
        "V": 3,
        "edges": [[0, 1], [1, 2]],
        "start": 0,
        "end": 2,
        "expected": 2
    },
    {
        "V": 4,
        "edges": [[0, 1], [1, 2]],
        "start": 2,
        "end": 3,
        "expected": -1
    }
]

for i, test in enumerate(test_cases, 1):
    result = shortest_path_length(test["V"], test["edges"], test["start"], test["end"])
    print(f"Test Case {i}: Output = {result}, Expected = {test['expected']}, {'✅' if result == test['expected'] else '❌'}")
