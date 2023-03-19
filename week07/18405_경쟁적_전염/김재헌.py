from collections import deque

n, k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

viruses = [[] for _ in range(k + 1)]
graph = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            viruses[graph[i][j]].append((i, j))

que = deque([])
for virusNum in range(1, k + 1):
    for x, y in viruses[virusNum]:
        que.append([x, y, virusNum])
second = 0
while que:
    if second == S:
        break
    second += 1
    size = len(que)
    for _ in range(size):
        x, y, virusNum = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = virusNum
                que.append([nx, ny, virusNum])
                if nx == X - 1 and ny == Y - 1:
                    second = S
                    _ = size
                    break
print(graph[X - 1][Y - 1])
