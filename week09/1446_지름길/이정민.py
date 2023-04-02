import heapq
import math

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [math.inf] * (d+1)

for i in range(d):
    graph[i].append((i+1,1))

for i in range(n):
    start, end, length = map(int,input().split())
    if end > d:
        continue
    graph[start].append((end, length))

def dijstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, cur = heapq.heappop(queue)

        if dist > distance[cur]:
            continue

        for g in graph[cur]:
            value = dist + g[1]
            if value < distance[g[0]]:
                distance[g[0]] = value
                heapq.heappush(queue, (value, g[0]))

dijstra(0)
print(distance[d])