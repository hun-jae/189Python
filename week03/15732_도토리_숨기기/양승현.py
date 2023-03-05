N, K, D = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(K)]

# consider filtering case : not (start <= end)
prev_cnt = lambda n: sum(filter(lambda k: 0 < k, [1 + (min(n, x[1])-x[0])//x[2] for x in info]))

l, r = 1, N+1
while l < r:
    mid = (l+r) // 2
    if prev_cnt(mid) >= D:
        r = mid
    else:
        l = mid + 1

print(l)