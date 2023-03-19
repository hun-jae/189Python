from collections import deque
#0에서 15까지... 이진법으로
bin = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]

N,M = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(map(int, input().split())))

#인접한 방 확인용 배열
map = [[0 for _ in range(N)]for _ in range(M)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

queue = deque()
def bfs(loc, cnt):
    queue.append(loc)
    while queue:
        cur = queue.popleft()
        y = cur[0]
        x = cur[1]
        map[y][x] = cnt
        for i in range(4):
            if bin[board[y][x]][i] == 0:
                tmp_y = y + dy[i]
                tmp_x = x + dx[i]
                if tmp_y > -1 and tmp_x > -1 and tmp_y <M and tmp_x < N and map[tmp_y][tmp_x]==0:
                    queue.append((tmp_y,tmp_x))

cnt = 1
for i in range(M):
    for j in range(N):
        if map[i][j] == 0:
            bfs((i, j), cnt)
            cnt += 1

sizes = [0]*(cnt)
for i in range(M):
    for j in range(N):
        sizes[map[i][j]] += 1


largest = 0

#인접한 방 중에 벽 부술 경우 합이 가장 큰 경우 찾기
for i in range(M):
    for j in range(N):
        cur_room = map[i][j]
        for d in range(4):
            tmp_y = i + dy[d]
            tmp_x = j + dx[d]
            if tmp_y > -1 and tmp_x > -1 and tmp_y < M and tmp_x < N:
                tmp_room = map[tmp_y][tmp_x]
                if cur_room == tmp_room:
                    continue
                else:
                    largest = max(largest, sizes[cur_room]+sizes[tmp_room])

print(cnt-1)
print(max(sizes))
print(largest)
