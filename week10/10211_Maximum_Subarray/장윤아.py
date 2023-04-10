t = int(input())
for test_case in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [0]*n
    dp[0] = nums[0] #이부분 때문에..!!
    for i in range(1, n):
        dp[i] = max(dp[i-1]+nums[i], nums[i])

    print(max(dp))
