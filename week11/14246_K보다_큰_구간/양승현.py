from itertools import accumulate

n, nums, k = int(input()), list(map(int, input().split())), int(input())
acc = [0] + list(accumulate(nums))

cnt, left = 0, 0
for r_num in acc:
    while k < r_num - acc[left]:
        left += 1
    cnt += left

print(cnt)
