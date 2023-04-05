T = int(input())
for tc in range(T):
    n = int(input())
    org_array = list(map(int,input().split()))
    dp = [0]
    for idx, i in enumerate(org_array):
        dp.append(max(dp[idx] + i, 0))
    ans = max(dp)
    print(ans if ans != 0 else max(org_array))