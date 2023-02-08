from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(x) for x in input().split()]
# handle stack right to be sorted by key<=count
cnt, right, res = Counter(nums), [], []

for i in range(N-1, -1, -1):
    while right and cnt[right[-1]] <= cnt[nums[i]]:
        right.pop()

    res.append(right[-1] if right else -1)
    right.append(nums[i])

for n in res[::-1]: print(n, end=' ')

