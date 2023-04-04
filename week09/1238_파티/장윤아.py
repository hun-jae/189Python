import heapq
n, m, x = map(int, input().split())
info = {i:[] for i in range(1, n+1)}
for i in range(m):
    start, end, time = map(int, input().split())
    info[start].append([end, time])

def dijkstra(start):
    q = []
    distance = [int(1e9)]*(n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist : continue

        for e, t in info[node]:
            cost = dist + t
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))

    return distance

res = [0]*(n+1)
for i in range(1, n+1):
    if i == x:
        xToOthers = dijkstra(i)
        for k in range(1, n+1):
            res[k] += xToOthers[k]
    else:
        res[i] += dijkstra(i)[x]

print(max(res))





# n, m, x = map(int, input().split())
# info = []
# for i in range(m):
#     start, end, time = map(int, input().split())
#     info.append([start, end, time])

# #플로이드
# distance = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
# for s, e, t in info:
#     distance[s][e] = t

# for i in range(1, n+1):
#     distance[i][i] = 0

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# time = []
# for i in range(1, n+1):
#     time.append(distance[i][x] + distance[x][i])

# print(max(time))
