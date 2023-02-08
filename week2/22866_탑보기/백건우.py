import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
buildings = deque(map(int,input().split()))
canSee = [0 for _ in range(N)]
minDis = [[INF,INF] for _ in range(N)]  #거리, 건물 번호
for i in range(len(buildings)):         #완전 탐색으로 풀이할시 N*N 시간초과 발생
    # 왼쪽 탐색
    for j in range(i-1, -1, -1):
        if buildings[i] <= buildings[j] :
            break
        elif buildings[i] > buildings[j] :
            if i - j < minDis[j][0] :
                minDis[j][0] = i - j
                minDis[j][1] = i+1
            canSee[j] += 1
    # 오른쪽 탐색
    for j in range(i+1,len(buildings)):
        if buildings[i] <= buildings[j] :
            break
        elif buildings[i] > buildings[j] :
            if j - i < minDis[j][0] :
                minDis[j][0] = j - i
                minDis[j][1] = i+1
            canSee[j] += 1


for idx, dis in enumerate(minDis):
    if dis[0] == INF :
        print("0")
    else :
        print('{} {}'.format(canSee[idx],dis[1]))
