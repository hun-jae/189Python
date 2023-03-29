n=range(int(input()))
g=[list(map(int, input().split()))for _ in n]
for m in n:
    for s in n:
        for t in n:
            g[s][t]=g[s][t]|(g[s][m]&g[m][t])
for l in g:
    print(*l)
