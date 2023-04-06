# 누적합 사용
# prefix_sum없애려면 맨앞열에 0 추가해줘야함(굳이?)
# -> 0번부터 말고 1번부터 하면 prefix_sum 변수 없앨 수 있음
N, K = map(int, input().split())
dp = [[1 for _ in range(N+1)] for _ in range(K)]
for i in range(1, K):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[K-1][N] % 1000000000)