N, D = map(int, input().split())
short = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)
for i in range(N):
    s, t, d = map(int, input().split())
    if t > D or t-s <= d:
        continue
    short[s].append((t, d))
distance[0] = 0
for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    for t, d in short[i]:
        distance[t] = min(distance[t], distance[i] + d)
print(distance[-1])