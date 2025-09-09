from collections import defaultdict

def contains_cycle(V, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:

                return True
        return False

    for i in range(V):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False

print(contains_cycle(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]))
print(contains_cycle(3, [[0, 1], [1, 2]]))                         
print(contains_cycle(4, [[0, 1], [1, 2], [2, 0]]))
