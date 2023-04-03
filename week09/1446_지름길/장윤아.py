import heapq
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append([i+1, 1])

def dijkstra(start):
    q = []
    distance = [int(1e9)]*(D+1)
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        d, node = heapq.heappop(q)
        if distance[node] < d : continue

        for item in graph[node]:
            cost = d + item[1]
            if distance[item[0]] > cost:
                distance[item[0]] = cost
                heapq.heappush(q, [cost, item[0]])

    return distance[D]

for _ in range(N):
    start, end, dist = map(int, input().split())
    if end > D : continue
    graph[start].append([end, dist])
print(dijkstra(0))
