T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    dp = [0] * N

    for i in range(N):
        if dp[i-1] + X[i] > 0:
            dp[i] = dp[i-1] + X[i]
        else:
            dp[i] = 0
    if max(dp) == 0:
        print(max(X))
    else:
        print(max(dp))
