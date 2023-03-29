N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]

dist = [float('inf')] * (D+1)   # distance from origin
dist[0] = 0                     # no move at start

for i in range(D+1):
    # move 1: walk from the previous
    dist[i] = min(dist[i], dist[i - 1] + 1)
    
    # move 2: use shortcut if possible (and better)
    for s, e, c in shortcuts:   
        if i == s and e <= D:
            dist[e] = min(dist[e], dist[i]+c)

print(dist[D])
