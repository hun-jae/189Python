from collections import deque

N, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

S, X, Y = map(int,input().split())

#바이러스 번호가 빠른 순으로 전염시켜야 하니까 virus 배열에 위치 저장
virus = [()] * 1001
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus[board[i][j]] = virus[board[i][j]] + (i,j)

queue = deque()
#큐에 넣어줌
for v in range(1, 1001):
    if len(virus[v]) > 0:
        for i in range(0, len(virus[v]), 2):
            queue.append((virus[v][i], virus[v][i+1], v))

sub_queue = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(S):
    while queue:
        cur = queue.popleft()
        virus = cur[2]
        y = cur[0]
        x = cur[1]

        for j in range(4):
            tmp_y = y + dy[j]
            tmp_x = x + dx[j]
            if tmp_y > -1 and tmp_x > -1 and tmp_y < N and tmp_x < N and board[tmp_y][tmp_x] == 0:
                sub_queue.append((tmp_y, tmp_x, virus))
                board[tmp_y][tmp_x] = virus
    #회차만큼 반복시키기 위해서 sub_queue 사용
    for s in range(len(sub_queue)):
        tmp = sub_queue.popleft()
        queue.append(tmp)

print(board[X-1][Y-1])