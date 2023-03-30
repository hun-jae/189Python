for tc in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    distance = [0] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    def bellman_ford():
        for i in range(n):
            for j in range((2*m)+w):
                cur, next, cost = edges[j]
                if distance[next] > distance[cur] + cost:
                    distance[next] = distance[cur] + cost
                    if i == n - 1:
                        return True
        return False

    if bellman_ford():
        print("YES")
    else:
        print("NO")
