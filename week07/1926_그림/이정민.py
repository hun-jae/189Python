from collections import deque

n,m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

dq = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

size = 0

def bfs(board, start):
    global size
    dq.append(start)
    board[start[0]][start[1]] = 0
    cnt = 0
    while dq:
        cur = dq.popleft()
        cnt += 1

        size = max(size, cnt)

        for i in range(4):
            tmp_y = cur[0] + dy[i]
            tmp_x = cur[1] + dx[i]
            if tmp_x > -1 and tmp_y > -1 and tmp_x < m and tmp_y < n and board[tmp_y][tmp_x] == 1:
                tmp = tmp_y, tmp_x
                board[tmp_y][tmp_x] = 0
                dq.append(tmp)

count = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            count += 1
            bfs(board, (i,j))

print(count)
print(size)