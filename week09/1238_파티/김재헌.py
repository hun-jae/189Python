from heapq import heappush as hpush, heappop as hpop

N, M, X = map(int, input().split())
INF = int(1e9)
adj_list = [[] for _ in range(N + 1)]
r_adj_list = [[] for _ in range(N + 1)]

for i in range(M):
    s, e, t = map(int, input().split())
    adj_list[s].append((e, t))
    r_adj_list[e].append((s, t))


def dij(start, flag):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    adj = adj_list if flag else r_adj_list
    q = []
    hpush(q, (start, 0))
    while q:
        node, dist = hpop(q)
        if distance[node] < dist:
            continue
        for v, t in adj[node]:
            cost = distance[node] + t
            if cost < distance[v]:
                distance[v] = cost
                hpush(q, (v, cost))
    return distance


dis = dij(X, True)
r_dis = dij(X, False)
print(max([dis[i] + r_dis[i] for i in range(1, N + 1)]))
