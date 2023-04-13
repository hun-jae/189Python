n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
k = int(input())

for i in range(n):
    arr[i] += arr[i-1]
left = -1
right = 0
cnt = 0
while True:
    val = arr[right] - arr[left]
    if val > k:
        cnt += n - right
        left += 1

    elif val <= k:
        right += 1
        if right == n:
            break
print(cnt)