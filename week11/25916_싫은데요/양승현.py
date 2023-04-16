from itertools import accumulate

_, vol = map(int, input().split())
nums = [int(x) for x in input().split()]

acc = [0] + list(accumulate(nums))
opt, left = 0, 0

for r_num in acc:
    while vol < r_num - acc[left]:
        left += 1
    opt = max(opt, r_num - acc[left])

print(opt)
