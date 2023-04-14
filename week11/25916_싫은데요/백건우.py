# sum때문에 시간 복잡도 증가?

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

holes = list(map(int, input().split()))
arr = [0 for _ in range(n+1)]
for i in range(1, n+1):
    arr[i] = arr[i-1] + holes[i-1]
left = ans = 0
right = 1
while right <= n :
    # cur = sum(holes[left:right+1]) 원래 이걸로 했다가 시간초과나서 누적합 배열로 
    cur = arr[right] - arr[left]
    if cur > m :
        left += 1
    else :
        ans = max(ans, cur)
        right += 1
print(ans)
