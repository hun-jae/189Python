N = int(input())
graph = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[None for _ in range(1 << N)] for _ in range(N)]
all_ = (1 << N)-1

def bt(cur, vis):

    if vis == all_:
        if graph[cur][0]:
            return graph[cur][0]
        return float('inf')

    if dp[cur][vis]:
        return dp[cur][vis]

    res = float('inf')
    for next_ in range(1, N):
        if graph[cur][next_] and not (1 << next_) & vis:
            res = min(res, graph[cur][next_] + bt(next_, vis | (1 << next_)))

    dp[cur][vis] = res
    return dp[cur][vis]


print(bt(0, 1))
