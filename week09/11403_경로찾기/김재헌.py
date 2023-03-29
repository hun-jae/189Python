n = int(input())
adj_graph = [list(map(int, input().split())) for _ in range(n)]

for m in range(n):
    for s in range(n):
        for t in range(n):
            adj_graph[s][t] = 1 if adj_graph[s][t] or (adj_graph[s][m] and adj_graph[m][t]) else 0

for l in adj_graph:
    for i in l:
        print(i, end=" ")
    print()