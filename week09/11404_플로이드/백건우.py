import heapq
import sys

INF = sys.maxsize

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    l, r, c = map(int,input().split())
    bus[l].append([r,c])

def dijk(start) :
    q = []
    heapq.heappush(q,[0, start])
    minDis = [INF for _ in range(n+1)]
    minDis[start] = 0
    while q :
        w, cur = heapq.heappop(q)
        if minDis[cur] < w : # 다른 방법으로 가는 경우로 인해 갱신된 minDis의 값이 현재의 방법으로 갈 때의 cost w 보다 작으면 현재의 방법을 탐색할 필요가 없음
            continue
        for nextNode, weight in bus[cur]:
            cost = w+weight
            if cost < minDis[nextNode] :
                minDis[nextNode] = cost
                heapq.heappush(q,[cost, nextNode]) # nextNode까지 가는 cost를 갱신한다.
    for i in range(1, n+1):
        if minDis[i] == INF : board[start][i] = 0
        else : board[start][i] = minDis[i]

for i in range(1, n+1):
    dijk(i)
for i in range(1, n+1):
    for j in range(1, n+1):
        print(board[i][j], end=" ")
    print()
