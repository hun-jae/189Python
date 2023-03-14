# 목표 위치를 기준으로 bfs를 돌린다.
from collections import deque

mv_y = [-1,0,1,0]
mv_x = [0,-1,0,1]

n, k = map(int, input().split())
board = []
visit = [[-1 for _ in range(n)] for _ in range(n)] # visit은 최단거리를 나타낸다.
for _ in range(n):
    board.append(list(map(int, input().split())))
s, ax, ay = map(int, input().split())

def bfs(y, x):
    global ans, minDis
    q = deque()
    q.append([y,x])
    visit[y][x] = 0
    if not board[y][x] == 0 :  # 목표위치에 이미 바이러스가 있으면 바로 정답을 갱신하고 bfs탐색하지 않는다.
        ans = board[y][x]
        return

    while q :
        py, px = q.popleft()
        for i in range(4):
            ny = py + mv_y[i]
            nx = px + mv_x[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n :
                continue
            if not visit[ny][nx] == -1 :
                continue
            if board[ny][nx] > 0 :  # 다음 스텝이 바이러스라면
                if visit[py][px] + 1 <= s and visit[py][px] + 1 <= minDis: # 한계 시간안에 도달할 수 있고 최단거리와 짧거나 같은 경우
                    minDis = visit[py][px] + 1 # 최단거리 갱신
                    if ans == 0 : # 지금까지 도달한 바이러스가 없으면 정답 갱신
                        ans = board[ny][nx]
                    elif ans > board[ny][nx] : # 최단 거리가 같더라도 번호가 낮은 바이러스가 우선순위 더 높다.
                        ans = board[ny][nx]
            visit[ny][nx] = visit[py][px] + 1
            q.append([ny,nx])

ans = 0
minDis = 100000000
bfs(ax-1,ay-1)  # bfs 
print(ans)
