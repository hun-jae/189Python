#k-1개를 이용해서 0~n을 만드는 방법에서 (1개를 더하면) k개를 이용해서 n을 만드는 수
#dp[1][0] = 1 ... dp[1][n] = 1
#dp[2][0] = 1 ... dp[2][n] = sum(dp[1][:n+1])

#dp[k][0] = dp[k-1][0]
#dp[k][x] = dp[k-1][0] + ... + dp[k-1][x]
#dp[k][n] = dp[k-1][0] + ... + dp[k-1][x] + ... + dp[k-1][n]

N, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(K)]
for i in range(1, K):
    for j in range(N+1):
        dp[i][j] = sum(dp[i-1][:j+1])
print(dp[K-1][N] % 1000000000)