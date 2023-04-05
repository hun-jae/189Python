# common LIS, naive solution: O(N^2)
N = int(input())
nums = [int(x) for x in input().split()]
dp = [1 for _ in range(N)]

for cur in range(N):
    for prev in range(0, cur):
        if nums[cur] < nums[prev]:
            dp[cur] = max(dp[cur], dp[prev] + 1)

print(max(dp))
