# 누적합 사용      cnt없애려면 맨앞열에 0 추가해줘야함(굳이?)
N, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(K)]
for i in range(1, K):
    cnt = 0
    for j in range(N+1):
        dp[i][j] = cnt + dp[i-1][j]
        cnt = dp[i][j]
print(dp[K-1][N] % 1000000000)