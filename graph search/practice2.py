# 미로 탈출
# N x M 크기의 정사각형 형태의 미로에 갇혀 있다.
# 시작 위치는 (1, 1) 이고 미로의 출구는 (N, M)이다.
# 미로의 0으로는 갈 수 없고 1로만 갈 수 있다.
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 출력하라

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()

    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print(graph)
    
    return graph[n - 1][m - 1]

print(bfs(0, 0))