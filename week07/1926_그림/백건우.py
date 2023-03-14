from collections import deque

# 이동용 리스트
mv_y = [-1,0,1,0] 
mv_x = [0,-1,0,1]

n, m = map(int, input().split())

board = []
visit = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    board.append(list(map(int,input().split())))

def bfs(y, x):
    global cntArea
    q = deque()
    q.append([y,x])
    visit[y][x] = True
    cnt = 1 # 현재 그림의 영역
    while q:
        py, px = q.popleft()
        for i in range(4):
            ny = py + mv_y[i]
            nx = px + mv_x[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m :
                continue
            if visit[ny][nx] :
                continue
            if board[ny][nx] == 0 :
                continue
            visit[ny][nx] = True
            q.append([ny,nx])
            cnt += 1  # 다음 스텝이 존재 하니까 그림의 영역 + 1
    cntArea = max(cntArea,cnt) # 그림의 최대 영역 갱신

cntArt = 0
cntArea = 0
for y in range(n):
    for x in range(m):
        if not visit[y][x] and board[y][x] == 1 :  
            cntArt += 1 # 현재 그림을 탐색하면 그림의 모든 영역을 순회하므로 같은 그림을 다시 탐색하는 일이 없다. 따라서 탐색횟수 = 그림의 
            bfs(y,x)
print(cntArt)
print(cntArea)
