from itertools import accumulate

n, m = map(int, input().split())
arr = list(map(int, input().split()))

acc = [0] + list(accumulate(arr))

max_ = 0

for right in range(m, n+1):
    left = right - m
    sub_acc = acc[right] - acc[left]
    max_ = max(max_, sub_acc)

print(max_)
