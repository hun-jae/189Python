N = int(input())
nums = [int(input()) for _ in range(N)]

total_sum = sum(nums)
l, r, side = 0, 0, 0
max_dist = 0

while l < N:
    while side < total_sum - side:
        side += nums[r]
        r = (r + 1) % N

    cur_dist = min(side, total_sum - side)
    max_dist = max(max_dist, cur_dist)

    side -= nums[l]
    l += 1

print(max_dist)
