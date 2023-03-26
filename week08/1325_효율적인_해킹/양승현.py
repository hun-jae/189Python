"""
O(N) 시간 안에 해결하고 싶었는데 실패함 ...
결국 naive하게 O(N^2)으로 전부 탐색함 -> 이게 pass..?
"""

import sys
input = sys.stdin.readline
from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(n):
    q, cnt = deque([n]), 0
    vis = [False] * (N+1)       # set 사용하면 시간 초과
    vis[n] = True

    while q:
        n = q.popleft()

        cnt += 1
        for next_ in graph[n]:
            if vis[next_]: continue
            vis[next_] = True
            q.append(next_)

    return cnt

max_cnt, max_nodes = 0, []
for k in range(1, N+1):
    cur_cnt = bfs(k)

    if cur_cnt == max_cnt:      # 최대값이 여러개일 수 있음
        max_nodes.append(k)
    elif max_cnt < cur_cnt:     # 최대값이 갱신될 때
        max_cnt = cur_cnt
        max_nodes = [k]

print(*max_nodes)
