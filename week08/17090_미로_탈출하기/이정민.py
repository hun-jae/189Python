import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

can = [[False for i in range (M)] for j in range(N)]
cnt = 0

def dfs(y, x):
    global cnt
    if visited[y][x] == True:
        return
    visited[y][x] = True

    if board[y][x] == 'U':
        idx = 0
    elif board[y][x] == 'R':
        idx = 1
    elif board[y][x] == 'D':
        idx = 2
    elif board[y][x] == 'L':
        idx = 3
    ny = y + dy[idx]
    nx = x + dx[idx]

    if ny < 0 or nx < 0 or ny >= N or nx >= M:
        can[y][x] = True
        cnt += 1
    else:
        dfs(ny, nx)

for i in range(N):
    for j in range(M):
        visited = [[False for i in range(M)] for j in range(N)]

        if can[i][j] == True:
            cnt +=1
        else:
            dfs(i,j)

print(cnt)