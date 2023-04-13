# 누적합한뒤 빼는데 반을 넘어가면 줄이고
# 반이 안되면늘리자
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.append(0)
for i in range(n):
    arr[i] += arr[i-1]
m = arr[-2]//2

left = -1
right = 0
max_ = 0
while True:
    val = arr[right] - arr[left]
    if val > m:
        max_ = max(max_, n-val)
        left += 1
    elif val == m:
        max_ = m
        break
    elif val < m:
        max_ = max(max_, val)
        if right < n:
            right += 1
        else:
            break
print(max_)