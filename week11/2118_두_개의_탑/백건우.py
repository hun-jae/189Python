"""
pypy로만 통과함. left랑 right를 어떤 기준으로 증가시킬지 몰라서 브루트포스 느낌으로 구현함.
"""

n = int(input())
dis = [int(input()) for _ in range(n)]

arr = [0 for _ in range(n)]
for i in range(1, n):
    arr[i] = arr[i-1] + dis[i-1]

total = sum(dis)
ans = 0
for right in range(1, n):
    for left in range(0, right):
        asc = arr[right] - arr[left]
        desc = total - asc
        cur = min(asc, desc)
        if ans < cur :
            ans = cur
print(ans)
