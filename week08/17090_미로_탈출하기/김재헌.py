import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]
move = {'U' : (-1, 0), 'R' : (0, 1), 'D' : (1, 0), 'L' : (0, -1)}
def dfs(x, y):
    if graph[x][y] == True:
        return True
    elif graph[x][y] == False:
        return False
    else:
        nx = x + move[graph[x][y]][0]
        ny = y + move[graph[x][y]][1]
        if 0 <= nx < n and 0 <= ny < m: #들어갈 수 있을때
            graph[x][y] = False
            graph[x][y] = dfs(nx, ny)
            return graph[x][y]
        else:
            return True

result = 0
for x in range(n):
    for y in range(m):
        if(dfs(x, y)):
            result += 1

print(result)