n, m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]
l = 0
r = pow(10, 9)
# mid 개의 보석씩 주면 x명한테 줄 수 있다고 할 때
# x가 n보다 크면 k를 줄이자
# n이 x보다 크면 k를 늘리자
# x==n이면 k를 줄이자
while l <= r:
    mid = (l + r) // 2
    x = 0
    if mid == 0: #만약 r==1이 된다면 1을 출력
        x = n+1
        break
    for j in jewels:
        if j % mid != 0:
            x += j // mid + 1
        else:
            x += j // mid

    if x > n:
        l = mid + 1
    elif x <= n:
        r = mid - 1
if x > n:
    print(mid + 1)
else:
    print(mid)
# 다 끝났는데 만약 x가 n보다 크다면.. 그건 못줌
# x가 n보다 작다면 가능
# x가 n이랑 같다면 가능
