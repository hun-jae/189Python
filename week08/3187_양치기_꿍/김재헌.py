import sys
sys.setrecursionlimit(100000)
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
sum_k = sum_v = 0
def dfs(x, y):

    v = k = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny]!="#":
            next_val = graph[nx][ny]
            if next_val == "v":
                v += 1
            elif next_val == "k":
                k += 1
            graph[nx][ny] = "#"
            nv, nk = dfs(nx, ny)
            v += nv
            k += nk
    return v, k

for x in range(R):
    for y in range(C):
        if graph[x][y] == "v" or graph[x][y] == "k":
            v = k = 0
            if graph[x][y] == "v":
                v = 1
            else:
                k = 1
            graph[x][y] = "#"
            nv, nk = dfs(x, y)
            v += nv
            k += nk

            if k > v:
                sum_k += k
            else:
                sum_v += v
print(sum_k, sum_v)