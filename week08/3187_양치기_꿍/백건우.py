import sys
sys.setrecursionlimit(10**9)

mv_y = [-1,0,1,0]
mv_x = [0,-1,0,1]

r, c = map(int,input().split())
board = []
visit = [[False for _ in range(c)] for _ in range(r)]
for _ in range(r):
    board.append(list(input()))

def dfs(y,x):
    global cntV, cntK
    visit[y][x] = True
    if board[y][x] == 'v' : cntV += 1
    elif board[y][x] == 'k' : cntK += 1
    for i in range(4):
        ny = y + mv_y[i]
        nx = x + mv_x[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c :
            continue
        if visit[ny][nx] or board[ny][nx] == '#':
            continue
        dfs(ny,nx)


ansK = 0 # 양
ansV = 0 # 늑대
for y in range(r):
    for x in range(c):
        if board[y][x] != '#' and not visit[y][x]:
            cntV, cntK = 0, 0
            dfs(y,x)
            if cntK > cntV :
                ansK += cntK
            else :
                ansV += cntV
print('{} {}'.format(ansK, ansV))
