# dp[n][k] := 0~N 정수 K개를 더해 합이 N이 되는 경우의 수
# 이젠 O(KN)
MOD = 1_000_000_000
N, K = map(int, input().split())
dp = [[1 for _ in range(K+1)] for _ in range(N+1)]
for j in range(1, K+1): dp[1][j] = j

for k in range(2, K+1):
    for n in range(2, N+1):
        # dp[n][k] = sum([dp[n-i][k-1] for i in range(n+1)]) % MOD
        dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % MOD
        
print(dp[N][K])
