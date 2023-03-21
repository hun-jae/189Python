#실패ㅠ
from collections import deque
N, K = map(int, input().split()) #map길이, k개 바이러스
#board 입력받기
board = []
q = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0: #바이러스
            q.append([tmp[j],i,j])
    board.append(tmp)
S, X, Y = map(int, input().split())
q.sort()
q = deque(q)
#좌표를 0,0부터 시작하기 위해 수정
X -= 1
Y -= 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(time):
    global board, q
    while q:
        length = len(q)
        time += 1
        for _ in range(length):
            virusNum, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] != 0 : continue

                board[nx][ny] = virusNum
                q.append([virusNum,nx,ny])
        if time == S: return

time = 0
bfs(time)

if board[X][Y] == 0:
    print(0)
else:
    print(board[X][Y])

    
    
    
'''
#1
from collections import deque
N, K = map(int, input().split()) #map길이, k개 바이러스
startPoint = [[0,0] for _ in range(K+1)] #i번 인덱스에 i번 바이러스의 시작점
#board 입력받기
board = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0: #바이러스
            startPoint[tmp[j]] = [i,j]
    board.append(tmp)
S, X, Y = map(int, input().split())

#좌표를 0,0부터 시작하기 위해 수정
X -= 1
Y -= 1

qInfo = {i: deque() for i in range(1, K+1)}
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(virusNum, i, j):
    global board, qInfo
    visited = [[0]*N for _ in range(N)]
    qInfo[virusNum].append((i,j))
    visited[i][j] = 1

    length = len(qInfo[virusNum])
    while qInfo[virusNum]:
        for _ in range(length):
            x, y = qInfo[virusNum].popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] != 0: continue #이미 바이러스 존재
                if visited[nx][ny] == 1: continue #이미 방문

                board[nx][ny] = virusNum
                visited[nx][ny] = 1
                qInfo[virusNum].append((nx,ny))
        break

time = 0
while time < S:
    time += 1
    for virus in range(1, K+1):
        bfs(virus, startPoint[virus][0], startPoint[virus][1])

if board[X][Y] == 0:
    print(0)
else:
    print(board[X][Y])
'''

'''
#2
from collections import deque
N, K = map(int, input().split()) #map길이, k개 바이러스
startPoint = [[0,0] for _ in range(K+1)] #i번 인덱스에 i번 바이러스의 시작점
#board 입력받기
board = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0: #바이러스
            startPoint[tmp[j]] = [i,j]
    board.append(tmp)
S, X, Y = map(int, input().split())

#좌표를 0,0부터 시작하기 위해 수정
X -= 1
Y -= 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(time):
    global board
    q = deque()
    for i in range(1, K+1):
        q.append(startPoint[i])
    while q:
        length = len(q)
        time += 1
        for _ in range(length):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] != 0 :continue

                board[nx][ny] = board[x][y]
                q.append([nx,ny])
        if time == S: return

time = 0
bfs(time)

if board[X][Y] == 0:
    print(0)
else:
    print(board[X][Y])
'''
