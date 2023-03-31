import heapq
import sys

INF = sys.maxsize

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)] # 시작 지점 ~ 끝나는 지점
for i in range(d):
    graph[i].append([i+1, 1]) # 바로 다음 칸으로 이동하는 건 비용이 1이니까 전부 1로 초기화


def dijk(start):
    q = []
    heapq.heappush(q, [0,start])
    minDis[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if cost > minDis[now]: # 현재 지름길로 이동 했을 때의 비용이 이미 탐색한 경로보다 클 경우 넘어간다.
            continue
        for next in graph[now]: # next => 다음 이동 노드, 비용 (바로 다음 노드, 1) or (지름길로 이동할 수 있는 다음 경로, 지름길의 비용)
            weight = cost + next[1]
            if weight < minDis[next[0]] :
                minDis[next[0]] = weight
                heapq.heappush(q,[weight,next[0]])

road = []
for _ in range(n):
    start, end, cost = map(int, input().split())
    if end <= d: # 도착지보다 멀리 가는 지름길은 고려 x
        graph[start].append([end,cost]) # 지름길 추가
minDis = [INF for _ in range(d+1)]
dijk(0)
print(minDis[d])
