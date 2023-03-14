from collections import deque

mv_y = [0,-1,0,1] # 서, 북, 동, 남
mv_x = [-1,0,1,0]

n, m = map(int, input().split())
visit = [[False for _ in range(n)] for _ in range(m)]
boardNum = [[0 for _ in range(n)] for _ in range(m)]  # 지도를 구역별로 마스킹한다.
areaDict = {}  # 구역별 면적
board = []
for _ in range(m):
    board.append(list(map(int, input().split())))

def bfs(y,x):
    global maxArea
    visit[y][x] = True
    boardNum[y][x] = idxNum # 구역 마스킹
    q = deque()
    q.append([y,x])
    cnt = 1
    while q:
        py, px = q.popleft()
        canMove = [False for _ in range(4)]  # 벽의 위치
        curWall = board[py][px]
        for i in range(4) :     # 현재 위치에서 벽의 위치를 파악
            if curWall%2 == 1 :
                canMove[i] = True
            curWall //= 2
        for i in range(4):
            if canMove[i] : # 벽이 있으면 이동X
                continue
            ny = py + mv_y[i]
            nx = px + mv_x[i]
            if ny < 0 or ny >= m or nx < 0 or nx >= n :
                continue
            if visit[ny][nx] :
                continue
            visit[ny][nx] = True
            boardNum[ny][nx] = idxNum  #구역 마스킹
            q.append([ny,nx])
            cnt += 1  # 현재 구역의 넓이
    areaDict[idxNum] = cnt  # 구역별 면적을 저장
    maxArea = max(maxArea,cnt)


roomCnt = 0
maxArea = 0
idxNum = 1
for y in range(m):
    for x in range(n):
        if not visit[y][x] :
            roomCnt += 1  # bfs 도는 횟수 = 방의 개수
            bfs(y,x)
            idxNum += 1   # 구역 마스킹 숫자

brokenArea = 0    # 구역별 마스킹이 끝났으면 인접한 서로 다른 구역의 면적의 합을 구한다.
for y in range(m):
    for x in range(n):
        for i in range(4):
            ny = y + mv_y[i]
            nx = x + mv_x[i]
            if ny < 0 or ny >= m or nx < 0 or nx >= n :
                continue
            if not boardNum[y][x] == boardNum[ny][nx] :
                brokenArea = max(brokenArea, areaDict[boardNum[y][x]] + areaDict[boardNum[ny][nx]])
print(roomCnt)
print(maxArea)
print(brokenArea)
