n = int(input())
m = int(input())
distance = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    s, e, d = map(int, input().split())
    distance[s][e] = min(distance[s][e], d)

for mid in range(1,n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if s==e: continue
            distance[s][e] = min(distance[s][e], distance[s][mid] + distance[mid][e])
for line in distance[1:]:
    for d in line[1:]:
        print(d if d!=float('inf') else 0, end=" ")
    print()
