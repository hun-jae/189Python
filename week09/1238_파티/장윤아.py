#잠시 올려둠
n, m, x = map(int, input().split())
info = []
for i in range(m):
    start, end, time = map(int, input().split())
    info.append([start, end, time])

#플로이드
distance = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
for s, e, t in info:
    distance[s][e] = t

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
