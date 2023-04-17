n = int(input())
nums = list(map(int, input().split()))
k = int(input())
res = 0

if n == 1:
    if nums[0] > k:
        res = 1

elif n > 1:
    i, j = 0, 1
    total = nums[i]

    while i<=j and j<n:
        if total+nums[j] <= k:
            total += nums[j]
            j += 1

        elif total+nums[j] > k:
            res += (n-j)
            total -= nums[i]
            i += 1

print(res)
