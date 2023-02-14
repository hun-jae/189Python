import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

can_handle = lambda t_given: M <= sum([t_given//t for t in times])

l, r = 1, sys.maxsize+1
while l < r:
    mid = (l+r)//2
    if can_handle(mid):
        r = mid
    else:
        l = mid + 1

print(l)