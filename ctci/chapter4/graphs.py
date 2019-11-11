from collections import deque

def bfs(graph, start):
    queue = deque(start)
    visisted = { start: True }
    print(start, end = ' ')
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not n in visisted:
                visisted[n] = True
                queue.append(n)
                print(n, end=' ')
    
def dfs(graph, start):
    stack = list(start)
    visited = { start: True }
    print(start, end=' ')
    while stack:
        node = stack.pop()
        if not node in visited:
            visited[node] = True
            print(node, end=' ')
        for n in graph[node]:
            if not n in visited:
                stack.append(n)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['B', 'D']
    }
    bfs(graph, 'A')
    print()
    bfs(graph, 'B')
    print()
    bfs(graph, 'E')
    print()
    print('------------------')

    dfs(graph, 'A')
    print()
    print('------------------')
    




