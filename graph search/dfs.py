graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# 재귀함수는 내부적으로 스택으로 동작하기 때문에 스택 자료구조를 이용하는 대부분의 알고리즘은 재귀함수로 구현할 수 있다.
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)

dfs(graph, 1, visited)
