import math

N = int(input())

adj = []

for _ in range(N):
    adj.append(list(map(int, input().split())))

dist = [[0 for _ in range(N)] for _ in range(N)]


for i in range(0, N):
    for j in range(0, N):
        if adj[i][j]: dist[i][j] = adj[i][j]
        else : dist[i][j] = math.inf

for k in range(0,N):
    for i in range(0, N):
        for j in range(0, N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])



for i in range(N):
    for j in range(N):
        if dist[i][j] < math.inf: print(1, end = ' ')
        else: print(0, end= ' ')
    print()