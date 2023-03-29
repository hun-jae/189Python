# 문제를 잘 읽자.. => (단 도로는 방향이 없으며 웜홀은 방향이 있다.)

def bellman_ford(graph):
    dist = [0 for _ in graph]
    for _ in range(len(graph)):
        for u in range(1, len(graph)):
            for v, cost in enumerate(graph[u]):
                dist[v] = min(dist[v], dist[u]+cost)

    for u in range(1, len(graph)):
        for v, cost in enumerate(graph[u]):
            if dist[u]+cost < dist[v]: return True

    return False


T = int(input())
for tc in range(1, T+1):
    N, M, W = map(int, input().split())
    graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[e][s] = graph[s][e] = min(graph[s][e], c)


    for _ in range(W):
        s, e, c = map(int, input().split())
        graph[s][e] = min(graph[s][e], -c)

    print("YES" if bellman_ford(graph) else "NO")
