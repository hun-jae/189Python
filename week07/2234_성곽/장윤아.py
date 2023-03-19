from collections import deque
N, M = map(int, input().split()) #M x N
board = [list(map(int, input().split())) for _ in range(M)]

#남동북서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[0]*N for _ in range(M)]
maxRoomSize = 0
totalRoomCnt = 0
combinedRoomSize = 0
nearbyRoomInfo = {}

def convertToBin(decimalNum):
    return bin(decimalNum)[2:].zfill(4)

def bfs(i,j):
    global visited
    roomCnt = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = totalRoomCnt

    while q:
        x, y = q.popleft()
        roomInfo = convertToBin(board[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=M or ny>=N : continue
            if roomInfo[i] == '1':
                # 가장자리가 아니면서 벽인 경우 인접한 방들을 저장
                if nearbyRoomInfo.get(totalRoomCnt) is None:
                    nearbyRoomInfo[totalRoomCnt] = set()
                nearbyRoomInfo[totalRoomCnt].add((nx,ny))
                continue
            if visited[nx][ny] != 0 : continue

            visited[nx][ny] = totalRoomCnt
            roomCnt += 1
            q.append((nx,ny))

    return roomCnt

roomSizeInfo = [0]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            totalRoomCnt += 1
            roomSize = bfs(i, j)
            roomSizeInfo.append(roomSize)
            maxRoomSize = max(maxRoomSize, roomSize)

print(totalRoomCnt)
print(maxRoomSize)
#여기까지 '그림' 문제와 동일
'''
어떤 방이 어떤 방과 인접해있는지 알면,
인접한 두 방 중 크기 합이 최대인 것을 구하면 된다고 생각
-> 가장자리가 아니면서 벽을 만났을 때 옆에 있는 방의 위치를 저장해서
'''
for i in range(1, totalRoomCnt+1):
    for x,y in nearbyRoomInfo[i]:
        if visited[x][y] != i:
            combinedRoomSize = max(combinedRoomSize, roomSizeInfo[i]+roomSizeInfo[visited[x][y]])

print(combinedRoomSize)
