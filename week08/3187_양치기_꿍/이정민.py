import sys
sys.setrecursionlimit(10**6)

R, C = map(int,input().split())

board = []

for _ in range(R):
    board.append(list(input()))

sheep = 0
wolf = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

live_s = 0
live_w = 0

def dfs(y, x):
    global live_w
    global live_s

    if board[y][x] == '#':
        return
    if board[y][x] == 'k':
        live_s += 1
    elif board[y][x] =='v':
        live_w += 1
    board[y][x] = '#'
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny > -1 and nx > -1 and ny < R and nx < C and board[ny][nx] != '#':
            dfs(ny, nx)

for i in range(R):
    for j in range(C):
        if board[i][j] != '#':
            live_s = 0
            live_w = 0
            dfs(i,j)
            if live_w >= live_s:
                wolf += live_w
            else:
                sheep += live_s

print(sheep, end=' ')
print(wolf)