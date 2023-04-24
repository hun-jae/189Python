n, k = map(int, input().split()) # k 연속적인 날짜의 수
nums = list(map(int,input().split()))

l = 0
r = k
ans = sum(nums[:r])
temp = ans
while r < n :
    temp -= nums[l]
    temp += nums[r]
    l += 1
    r += 1
    ans = max(ans, temp)
print(ans)
