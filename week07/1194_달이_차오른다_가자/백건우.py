from collections import deque
from queue import PriorityQueue

mv_y = [-1,0,1,0]
mv_x = [0,-1,0,1]

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

visit = deque([[{} for _ in range(M)] for _ in range(N)])  # visit을 dict로 설정해 보유한 열쇠를 키값으로 삼음
q=deque()

# 입력 부분
for y in range(N):
    for x in range(M):
        if board[y][x] == '0':
            q.append([y,x,['x'],0])   # 0 이 시작위치
            visit[y][x]['x'] = True
            break
    if q : # 시작위치 파악했으면 나간다.
        break

while q: # bfs 시작
    y, x, curKeys, curMv = q.popleft()  # 현재 y, 현재 x, 현재 보유한 열쇠, 현재 이동거리
    keyStr = ''.join(sorted(curKeys))   # 현재 보유한 열쇠를 visit의 key값으로 쓰기 위해 문자열로 만든다.
    for i in range(4):
        ny = y + mv_y[i]
        nx = x + mv_x[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M : # 범위 벗어남
            continue
        if board[ny][nx] == '1': # 목적지 도달
            print(curMv+1)
            exit(0)
        if board[ny][nx] == '#': # 벽은 이동 불가
            continue
        # 문인데 이동불가능한지 파악
        if board[ny][nx] == 'A' and not 'a' in curKeys: 
            continue
        if board[ny][nx] == 'B' and not 'b' in curKeys:
            continue
        if board[ny][nx] == 'C' and not 'c' in curKeys:
            continue
        if board[ny][nx] == 'D' and not 'd' in curKeys:
            continue
        if board[ny][nx] == 'E' and not 'e' in curKeys:
            continue
        if board[ny][nx] == 'F' and not 'f' in curKeys:
            continue
        if keyStr in visit[ny][nx]:
            continue
        # 다음 칸이 열쇠 칸이면 열쇠 추가한다.
        if board[ny][nx] == 'a':
            if 'a' in curKeys:    # 이미 갖고 있는 열쇠는 추가할 필요 없음
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else :  # 기존에 갖지 못한 열쇠면 열쇠 리스트에 추가한다.
                visit[ny][nx][''.join(sorted(curKeys+['a']))] = True # 추가한 열쇠리스트로 visit초기화
                q.append([ny, nx, curKeys + ['a'], curMv + 1])
            continue
        if board[ny][nx] == 'b':
            if 'b' in curKeys:
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else:
                visit[ny][nx][''.join(sorted(curKeys+['b']))] = True
                q.append([ny, nx, curKeys + ['b'], curMv + 1])
            continue
        if board[ny][nx] == 'c':
            if 'c' in curKeys:
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else:
                visit[ny][nx][''.join(sorted(curKeys+['c']))] = True
                q.append([ny, nx, curKeys + ['c'], curMv + 1])
            continue
        if board[ny][nx] == 'd':
            if 'd' in curKeys:
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else:
                visit[ny][nx][''.join(sorted(curKeys+['d']))] = True
                q.append([ny, nx, curKeys + ['d'], curMv + 1])
            continue
        if board[ny][nx] == 'e':
            if 'e' in curKeys:
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else:
                visit[ny][nx][''.join(sorted(curKeys+['e']))] = True
                q.append([ny, nx, curKeys + ['e'], curMv + 1])
            continue
        if board[ny][nx] == 'f':
            if 'f' in curKeys:
                visit[ny][nx][keyStr] = True
                q.append([ny, nx, curKeys, curMv + 1])
            else:
                visit[ny][nx][''.join(sorted(curKeys+['f']))] = True
                q.append([ny, nx, curKeys + ['f'], curMv + 1])
            continue
        q.append([ny, nx, curKeys, curMv+1])
        visit[ny][nx][keyStr]= True

print("-1")
