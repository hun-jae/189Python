# 누적합 사용      cnt없애려면 맨앞열에 0 추가해줘야함(굳이?)
N, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(K)]
for i in range(1, K):
    prefix_sum = 0
    for j in range(N+1):
        prefix_sum = dp[i][j] = prefix_sum + dp[i-1][j]
print(dp[K-1][N] % 1000000000)