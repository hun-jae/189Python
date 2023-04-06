INF = float('inf')
n = int(input())
w =[list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range((1 << n)-1)] for _ in range(n)]
def tsp(node, visited):

    if visited == (1<<n) - 1:
        return w[node][0] if w[node][0] else INF

    if dp[node][visited]: #현재 노드가 저장돼있다면
        return dp[node][visited]

    tmp = INF
    for i in range(n): #현재 노드가 저장이 안돼있다면
        if not visited & (1<<i) and w[node][i]:
            tmp = min(tmp, tsp(i, visited | (1 << i)) + w[node][i])
    dp[node][visited] = tmp
    return tmp
print(tsp(0, 1))
