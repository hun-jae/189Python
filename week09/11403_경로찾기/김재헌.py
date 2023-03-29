i,u=int,input
n=range(i(u()))
g=[list(map(i, u().split()))for _ in n]
for m in n:
 for s in n:
  for t in n:g[s][t]=g[s][t]|(g[s][m]&g[m][t])
for l in g:print(*l)

# n = range(int(input()))
# graph = [list(map(int, input().split())) for _ in n]
# for m in n:
#     for s in n:
#         for t in n:
#             graph[s][t] = graph[s][t] or (graph[s][m] and graph[m][t])
# for l in graph:
#     print(*l)