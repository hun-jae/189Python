for tc in range(int(input())):
    n, m, w = map(int, input().split())
    edges = []
    #INF로 초기화 했을 때 각 노드의 묶음? 마다 하나의 노드의 본인 distance를 0으로 초기화해야함
    #어차피 음수사이클의 존재만 판단하면 되기때문에 0으로 초기화해도 가능
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
