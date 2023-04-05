# using binary search : O(NlogN)
from bisect import bisect_left as bs

N = int(input())
nums = [-int(x) for x in input().split()]
dp = []

for n in nums:
    i = bs(dp, n)

    if i == len(dp): dp.append(n)
    else: dp[i] = n

print(len(dp))
