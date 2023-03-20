from collections import deque

mv_y = [-1,0,1,0]
mv_x = [0,-1,0,1]

n = int(input())
board = []
visit = [[[False for _ in range(n)] for _ in range(n)] for _ in range(2)] # visit에 통나무 가운데 좌표만 표시한다. 가로, 세로 상태 각각 visit배열을 만든다.
for _ in range(n):
    board.append(list(input()))

treeState = 0 # 0이 가로 1이 세로
endState = 0
tree = []
end = []
isFindTree = False
isFindEnd = False
for y in range(n) :
    for x in range(n):
        if board[y][x] == 'B' and not isFindTree:    # 나무 좌표
            if x + 1 < n and board[y][x+1] == 'B': # 가로인경우
                treeState = 0
                tree = [y,x+1]
            elif y + 1 < n and board[y+1][x] == 'B': # 세로인 경우
                treeState = 1
                tree = [y+1,x]
            isFindTree = True
        if board[y][x] == 'E' and not isFindEnd: # 종점 좌표
            if x+1 < n and board[y][x+1] == 'E': # 종점이 가로인 경우
                end = [y,x+1]
            elif y+1 < n and board[y+1][x] == 'E': # 종점이 세로인 
                endState = 1
                end = [y+1,x]
            isFindEnd = True

def canMove(idx): # 상하좌우 이동이 가능한지 파악
    if curState == 0 : # 가로일 때
        leftTreeY = curY   # 가로, 세로 상태와 가운데 통나무의 좌표를 알면 다른 통나무들의 좌표를 알 수 있다.
        leftTreeX = curX - 1
        ny = leftTreeY + mv_y[idx]
        nx = leftTreeX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >=n or board[ny][nx] == '1':
            return False

        ny = curY + mv_y[idx]
        nx = curX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        rightTreeY = curY
        rightTreeX = curX + 1
        ny = rightTreeY + mv_y[idx]
        nx = rightTreeX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False
    elif curState == 1 : # 세로일 때
        leftTreeY = curY - 1
        leftTreeX = curX
        ny = leftTreeY + mv_y[idx]
        nx = leftTreeX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = curY + mv_y[idx]
        nx = curX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        rightTreeY = curY + 1
        rightTreeX = curX
        ny = rightTreeY + mv_y[idx]
        nx = rightTreeX + mv_x[idx]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False
    return True

def canRotate(): # 회전 가능한지 
    if curState == 0 : # 가로일 때
        leftTreeY = curY
        leftTreeX = curX - 1
        rightTreeY = curY
        rightTreeX = curX + 1

        ny = leftTreeY - 1
        nx = leftTreeX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = leftTreeY + 1
        nx = leftTreeX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = curY - 1
        nx = curX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = curY + 1
        nx = curX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False


        ny = rightTreeY - 1
        nx = rightTreeX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = rightTreeY + 1
        nx = rightTreeX
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

    elif curState == 1 : # 세로일 때
        leftTreeY = curY - 1
        leftTreeX = curX
        rightTreeY = curY + 1
        rightTreeX = curX

        ny = leftTreeY
        nx = leftTreeX - 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = leftTreeY
        nx = leftTreeX + 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = curY
        nx = curX - 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = curY
        nx = curX + 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = rightTreeY
        nx = rightTreeX - 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False

        ny = rightTreeY
        nx = rightTreeX + 1
        if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == '1':
            return False
    return True

q = deque()
q.append(tree+[treeState,0])  # 가운데 나무 좌표, 현재 나무의 가로 세로 상태, 현재 스텝
visit[treeState][tree[0]][tree[1]] = True

while q:
    curY, curX, curState, cntMove = q.popleft()
    for i in range(4):
        if canMove(i) and not visit[curState][curY+mv_y[i]][curX+mv_x[i]] : # 상하좌우 이동가능한지 파악
            if end[0] == curY+mv_y[i] and end[1] == curX + mv_x[i] and endState == curState: # 종착지에 도달하면 출력하고 종료
                print(cntMove + 1 )
                exit(0)
            visit[curState][curY+mv_y[i]][curX+mv_x[i]] = True
            q.append([curY+mv_y[i], curX+mv_x[i],curState,cntMove+1])
    if canRotate() and not visit[(curState+1)%2][curY][curX] : # 회전 가능한지 파악
        if end[0] == curY and end[1] == curX and endState == (curState+1)%2 : # 종착지에 도달하면 종료
            print(cntMove + 1)
            exit(0)
        visit[(curState+1)%2][curY][curX] = True # 회저하면 가로세로 상태 변경
        q.append([curY,curX,(curState+1)%2,cntMove+1])
print("0") # 종착지에 도달 
