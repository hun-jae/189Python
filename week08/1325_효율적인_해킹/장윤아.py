from collections import deque

N, M = map(int, input().split())
board = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    b, a = map(int, input().split())
    board[a].append(b)

res = []

def bfs(i):
    q = deque()
    visited = [0] * (N + 1)
    q.append(i)
    visited[i] = 1
    cnt = 0

    while q:
        x = q.popleft()
        cnt += 1

        for item in board[x]:
            if visited[item] == 1: continue

            q.append(item)
            visited[item] = 1

    return cnt

tmp = []
for i in range(1, N+1):
    tmp.append((bfs(i), i))

tmp.sort(key = lambda x : (-x[0], x[1]))
maxVal = tmp[0][0]
for val, idx in tmp:
    if val == maxVal:
        res.append(idx)
    else: break

print(*res)
