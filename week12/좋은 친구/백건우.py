import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # k 연속적인 날짜의 수
nums = [len(input())-1 for _ in range(n)]

pair = [0 for _ in range(21)]
ans = 0
for i in range(k+1):
    if pair[nums[i]] > 0 :
        ans += pair[nums[i]]
    pair[nums[i]] += 1

l = 0
r = k+1
while r < n :
    pair[nums[l]] -= 1
    if pair[nums[r]] > 0 :
        ans += pair[nums[r]]
    pair[nums[r]] += 1
    l += 1
    r += 1
print(ans)
