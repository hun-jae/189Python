import heapq
import sys

INF = sys.maxsize

n, m, x =map(int,input().split())

town = [[] for _ in range(n+1)]

for _ in range(m):
    l, r, cost = map(int, input().split())
    town[l].append([r,cost])

def dijk(start):
    heapq.heappush(q,[0, start]) # 시작 마을 입력
    minDis[start] = 0
    while q :
        w, now = heapq.heappop(q)
        if minDis[now] < w : # 이전 탐색으로 갱신된 now까지 가는 경로의 비용(minDis[now])이 현재 now까지 가는 비용인 w보다 작으면 탐색할 필요가 없다.
            continue
        for next, cost in town[now]:
            nextCost = w + cost
            if minDis[next] > nextCost :
                minDis[next] = nextCost
                heapq.heappush(q,[nextCost, next])


goCost = [INF for _ in range(n+1)] # 모든 마을에서 목표 마을까지 가는 비용을 저장하기 위한 배열
for i in range(1, n+1): # 각 마을마다 탐색 진행
    if i == x : continue  # 목표마을이 시작점이 될 수 없다.
    minDis = [INF for _ in range(n + 1)]
    q = []
    dijk(i)
    goCost[i] = minDis[x] # 각 마을에서 탐색 완료했을 때 목표마을 까지의 비용을 저장한다.
minDis = [INF for _ in range(n + 1)]
dijk(x) # 목표마을에서 각 마을까지의 최소비용 구한다.
ans = 0
for i in range(1, n+1):
    if i == x : continue
    ans = max(ans, goCost[i]+minDis[i])
print(ans)
