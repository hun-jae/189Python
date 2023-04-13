n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
for i in range(n):
    arr[i] += arr[i-1]
left = -1
right = 0
max_ = 0
while True:
    val = arr[right] - arr[left]

    if val > m:
        left += 1
    elif val == m:
        max_ = max(max_, val)
        left += 1
    elif val < m:
        max_ = max(max_, val)
        if right < n:
            right += 1
        else:
            break
print(max_)