n, m = map(int, input().split())
edges = []
INF = int(1e9)
distance = [INF] * (n + 1)
distance[1] = 0
for _ in range(m):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

def bellman_ford():
    for i in range(n):
        for j in range(m):
            cur, next, cost = edges[j]
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n - 1:
                    return False
    return True

if bellman_ford():
    for i in distance[2:]:
        print(i if i != INF else -1)
else:
    print(-1)

