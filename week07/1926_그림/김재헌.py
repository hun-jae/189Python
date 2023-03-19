from collections import deque

n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [list(map(int, input().split())) for _ in range(n)]
max_ = 0
num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            graph[i][j] = 0
            que = deque([(i, j)])
            cnt = 1
            num += 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                        graph[nx][ny] = 0
                        que.append((nx, ny))
                        cnt += 1
            max_ = max(max_, cnt)
print(num)
print(max_)
