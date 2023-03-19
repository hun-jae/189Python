from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

cnt = 0
maxWidth = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    global visited
    tmpWidth = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            if visited[nx][ny] == 1 : continue

            if board[nx][ny] == 1:
                tmpWidth += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    return tmpWidth

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            maxWidth = max(maxWidth, bfs(i,j))
            cnt += 1

print(cnt)
print(maxWidth)
