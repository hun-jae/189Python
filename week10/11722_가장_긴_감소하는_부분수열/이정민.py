n = int(input())

a = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = 1
    else:
        max_len = 0
        for j in range(i):
            if a[j] > a[i]:
                max_len = max(max_len, dp[j])
        dp[i] = max_len + 1
print(max(dp))