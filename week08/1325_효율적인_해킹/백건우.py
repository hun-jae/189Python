# bfs로 풀었는데 pypy로만 통과함 dfs로 바꿔서 다시 풀 예정
# dfs로 풀려면 scc 알고리즘 사용해야함

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    tree[b].append(a)

def bfs(idx):
    global cnt
    visit[idx] = True
    q = deque([idx])
    cnt += 1
    while q:
        cur = q.popleft()
        for next in tree[cur]:
            if not visit[next]:
                visit[next] = True
                cnt += 1
                q.append(next)

maxHacked = 0
ans = []
for i in range(1, n+1):
    visit = [False for _ in range(n+1)]
    cnt = 0
    bfs(i)
    if maxHacked < cnt:
        maxHacked = cnt
        ans = [i]
    elif maxHacked == cnt:
        ans.append(i)

print(*sorted(ans))
