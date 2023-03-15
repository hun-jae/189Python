from collections import deque

N = int(input())
mat = [list(input()) for _ in range(N)]

d = 0       # 0: vertical, 1: horizontal
CHECK = {('U', 0): [(-2, 0)], ('U', 1): [(-1, -1), (-1, 0), (-1, 1)],
        ('D', 0): [( 2, 0)], ('D', 1): [( 1, -1), ( 1, 0), ( 1, 1)],
        ('L', 1): [(0, -2)], ('L', 0): [(-1, -1), (0, -1), (1, -1)],
        ('R', 1): [(0,  2)], ('R', 0): [(-1,  1), (0,  1), (1,  1)],
        ('T', 0): [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)],
        ('T', 1): [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]}

MOVE = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1], 'T': [0, 0]}

# find the init and target location
target, loc = [], []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'E':
            target.append((i, j))
        if mat[i][j] == 'B':
            loc.append((i, j))

ti, tj = map(lambda x: sum(x)//3, zip(*target))
si, sj = map(lambda x: sum(x)//3, zip(*loc))
sd = 1 if loc[0][0] == loc[1][0] else 0
td = 1 if target[0][0] == target[1][0] else 0

def bfs(si, sj, sd):
    q = deque([(si, sj, sd)])
    cost = 0
    vis = set()

    while q:
        sz = len(q)
        for _ in range(sz):
            i, j, d = q.popleft()
            if (i, j, d) in vis: continue
            vis.add((i, j, d))
            if (i, j, d) == (ti, tj, td): return cost

            for mv in ['U', 'D', 'L', 'R', 'T']:
                feas = True
                for di, dj in CHECK[(mv, d)]:
                    ci, cj = i+di, j+dj
                    if not (0<=ci<N and 0<=cj<N) or mat[ci][cj] == '1': feas = False

                di, dj = MOVE[mv]
                ni, nj = i+di, j+dj
                if feas: q.append((ni, nj, not d if mv == 'T' else d))

        cost += 1

res = bfs(si, sj, sd)
print(res if res else 0)
